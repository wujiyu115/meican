# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from functools import reduce

import requests
import random

from urls import *
from errcode import errcode as ErrCode
from errcode import desc as Desc

from util.utils import millis, empty_list
from util.obj_util import dict_obj, dict_item_obj
from util.cookie_util import load_cookies, save_cookies
from util.utils import milli_strftime
from util.mylog import debug, info, error
from util.configutil import ConfigUtil
from util.date_util import DateUtil
from message import Message
from msg import msg as Msg

SIGN_ERROR_FLAG = "username-field"
TIMEOUT = 10

class OrderTimeItem(object):
    """docstring for OrderTimeItem"""
    def __init__(self, hour, min):
        super(OrderTimeItem, self).__init__()
        self.hour = hour
        self.minute = min

class OrderDesc(object):
    """docstring for OrderDesc"""
    def __init__(self):
        super(OrderDesc, self).__init__()
        self.desc = ""

    def append_dish(self, dish_item, dish_count):
        self.desc = "%s name:[%s], price:[%s], count:[%s] |"%(self.desc, dish_item.name, int(dish_item.priceInCent/100), dish_count)

    def get_desc(self):
        return self.desc

class MeiCan:
    def __init__(self, username, password):
        self._session = requests.Session()
        self.login_ok = False
        self.close_time_list = []
        self.username = username
        self.password = password

    def get_close_time_lst(self):
        return self.close_time_list

    def get_order_time_lst(self):
        order_time = []
        close_lst = self.close_time_list
        for time_str in close_lst:
            t_item = time_str.split(":")
            hour, minute = DateUtil.date_diff_min(int(t_item[0]), int(t_item[1]), int(ConfigUtil.instance().ahead_min) * -1)
            order_time.append(OrderTimeItem(hour, minute))
            pass
        return order_time

    def load_mc_cookies(self):
        return load_cookies(self._session, ConfigUtil.instance().cookies)

    def save_mc_cookies(self):
        return save_cookies(self._session, ConfigUtil.instance().cookies)

    def login(self):
        code = self.load_mc_cookies()
        info("meican | init | has cookies:<%s>"%code)
        if code == False:
            code = self.login_account(self.username, self.password)
            if code != ErrCode.ok:
                error("meican | login error:<%s>"%Desc[code])
            else:
                self.save_mc_cookies()
                self.login_ok = True
        else:
            self.login_ok = True

        if self.login_ok:
            # mc_time_info = self.mc_time()
            # info("meican |server time | time:<%s>"%(milli_strftime(mc_time_info.serverTime, "%Y-%m-%d %H:%M:%S")))
            show_info = self.account_show_info()
            info("meican | login info | username:<%s>"%(show_info.username))
            self.close_time_list = self.tab_close_time()
            # info("meican | order limit times | <%s>"%(str(self.close_time_list)))
        return self.login_ok

    def login_account(self, username, password):
        form_data = {"username": username, "password": password, "loginType": "username", "remember": "true", "redirectUrl": ""}
        response = self.query("post", login_url(), form_data, True)
        if 200 != response.status_code or SIGN_ERROR_FLAG in response.content:
            return ErrCode.wrong_user
        return ErrCode.ok

    def query(self, method, url, data = None, ignore_login = False):
        debug(url)
        if ignore_login == False and self.login_ok == False :
            return False
        resp =  getattr(self._session, method)(url, data = data, timeout = TIMEOUT)
        debug(resp.content)
        return resp

    def get(self, url, data = None):
        return self.query("get", url, data)

    def post(self, url, data = None):
        return self.query("post", url, data)

    def account_show_info(self):
        usr_info = json.loads(self.get(account_show_url()).content)
        usr_info = dict_obj(usr_info)
        return usr_info

    def mc_time(self):
        mc_time_info = json.loads(self.get(mc_time_url()).content)
        mc_time_info = dict_obj(mc_time_info)
        return mc_time_info

    def calendar_items(self):
        return json.loads(self.get(calender_items_url()).content)

    def get_restaurants(self, tab):
        return json.loads(self.get(restaurants_url(tab)).content)['restaurantList']

    def get_recommends(self, tab):
        return json.loads(self.get(recommendations_url(tab)).content)

    def get_dish_list(self, tab, restaurant_uid):
        return json.loads(self.get(restaurant_dishes_url(tab, restaurant_uid)).content)['dishList']

    def order_request(self, tab, dish_ids, address_uid):
        return json.loads(self.post(order_url(tab, dish_ids, address_uid)).content)

    def recommends_dish_list(self, tab):
        re_net_datas = self.get_recommends(tab)
        re_net_datas = dict_obj(re_net_datas)
        re_lst = None
        dish_lst = None

        if not empty_list(re_net_datas.myRegularDishList) :
            re_lst = re_net_datas.myRegularDishList
        if ConfigUtil.instance().other_recommend == True and  not empty_list(re_net_datas.othersRegularDishList) :
            re_lst = re_lst or []
            re_lst = re_lst + re_net_datas.othersRegularDishList
        if not re_lst:
            return ErrCode.not_recommend, None
        dish_lst = filter(lambda x: x.priceInCent and x.restaurant.available == True, re_lst)

        if empty_list(dish_lst):
            return ErrCode.not_filter_recommend, None
        # name | priceInCent
        return ErrCode.ok, dish_lst

    def restaurant_dish_list(self, tab):
        restaurants = self.get_restaurants(tab)
        if empty_list(restaurants):
            return None
        restaurant_uid = restaurants[0]['uniqueId']
        dish_lst  =self.get_dish_list(tab, restaurant_uid)
        dish_lst = dict_item_obj(dish_lst)
        dish_lst = filter(lambda x: x.priceInCent , dish_lst)
        return dish_lst

    def tab_close_time(self):
        close_time_lst = []
        data_list = self.calendar_items()['dateList']
        for c_item in data_list[0]['calendarItemList']:
            close_time = c_item['openingTime']['closeTime']
            close_time_lst.append(close_time)
        return close_time_lst

    def available_tabs(self):
        data_list = self.calendar_items()['dateList']
        return reduce(lambda x, y: x + y, [filter(lambda x: x['status'] == 'AVAILABLE', _['calendarItemList'])
                                           for _ in data_list])
    def available_tab(self, index=0):
        tabs = self.available_tabs()
        if empty_list(tabs):
            return ErrCode.not_avilable_tabs, None
        tab_len = len(tabs)
        if index > tab_len - 1:
            return ErrCode.not_index_tabs, None

        tab = tabs[index]
        target_time = tab["targetTime"]
        mill = millis()
        if mill > target_time :
            error("meican | no_available_tab | now:<%s>, target_time:<%s>"%(mill, target_time))
            return ErrCode.not_right_time_tabs, None
        return ErrCode.ok, tab

    def gen_order_dish(self, dish_item, dis_count, order_desc):
        order_desc.append_dish(dish_item, dis_count)
        return {"count": dis_count,"dishId":int(dish_item.id)}

    def group_dish(self, limit_cent, dish_lst):
        # dish_lst.sort(key = lambda dish: dish.priceInCent, reverse = True)
        main_lst = []
        side_lst = []
        for dish_item in dish_lst:
            if dish_item.priceInCent > limit_cent * 0.6:
                main_lst.append(dish_item)
            else:
                side_lst.append(dish_item)

        dis_count = 1
        select_cent = 0
        select_dish = []
        order_desc = OrderDesc()

        main_index = random.randint(0, len(main_lst) - 1)
        side_lst.insert(0, main_lst[main_index])

        for dish_item in side_lst:
            next_cent = select_cent + dish_item.priceInCent
            if next_cent <= limit_cent:
                select_cent = next_cent
                select_dish.append(self.gen_order_dish(dish_item, dis_count, order_desc))
        return select_dish, order_desc

    def order_pack(self):
        code, tab = self.available_tab()
        if code != ErrCode.ok:
            return code
        user_tab_corp = tab['userTab']['corp']
        address_uid = user_tab_corp['addressList'][0]['uniqueId']
        price_limit_cent = user_tab_corp['priceLimitInCent']

        dish_ids = []
        desc_obj = None
        code, re_lsts = self.recommends_dish_list(tab)
        if code != ErrCode.ok:
            return code
        if not empty_list(re_lsts):
            dish_ids, desc_obj = self.group_dish(price_limit_cent, re_lsts)
        else:
            dish_lists = self.restaurant_dish_list(tab)
            dish_ids, desc_obj = self.group_dish(price_limit_cent, dish_lists)
        if empty_list(dish_ids):
            return ErrCode.money_dish_error
        resp = self.order_request(tab, dish_ids, address_uid)
        if resp["status"] == "SUCCESSFUL":
            info("meican | order success | <%s>"%desc_obj.get_desc())
            return ErrCode.ok
        return ErrCode.order_error

    def order(self):
        code = self.order_pack()
        if code != ErrCode.ok:
            info("meican | order failure, errdesc:<%s>"%Desc[code])
        return code