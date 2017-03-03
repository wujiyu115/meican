# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import datetime
import time

from util.utils import milli_strftime
from util.json_util import json_dump
import urllib

one_week = datetime.timedelta(weeks=1)

def meican_params(datas):
    d = {"noHttpGetCache": int(time.time() * 1000)}
    d.update(datas)
    p = "&".join(["{}={}".format(k, v) for (k, v) in d.items()])
    return p

def get_url(url):
    meican_url = "https://meican.com/{}"
    return meican_url.format(url)

def login_url():
    return get_url("account/directlogin")

def mc_time_url():
    return get_url("preorder/basic?{}".format(meican_params({})))

def account_show_url():
    return get_url("preorder/api/v2.1/accounts/show?{}".format(meican_params({})))

def calender_items_url():
    today = datetime.datetime.today()
    begin_date = str(today.date())
    end_date = str((today + one_week).date())
    data = {
        "beginDate": begin_date,
        "endDate": end_date,
        "withOrderDetail": False,
    }
    return get_url("preorder/api/v2.1/calendarItems/list?{}".format(meican_params(data)))

def concat_target_time(tab):
    return "%s %s"%(milli_strftime(tab["targetTime"]), tab["openingTime"]["closeTime"])

def restaurants_url(tab):
    uid = tab['userTab']['uniqueId']
    data = {
        "tabUniqueId": uid,
        "targetTime": concat_target_time(tab),
    }
    return get_url("preorder/api/v2.1/restaurants/list?{}".format(meican_params(data)))

def recommendations_url(tab):
    uid = tab['userTab']['uniqueId']
    data = {
        "tabUniqueId": uid,
        "targetTime": concat_target_time(tab),
    }
    return get_url("preorder/api/v2.1/recommendations/dishes?{}".format(meican_params(data)))


def order_url(tab, dish_ids, address_uid):
    d_str = json_dump(dish_ids)
    order_string = urllib.quote(d_str)
    # order_string = "%5B%7B%22count%22:1,%22dishId%22:{}%7D%5D".format(dish_id)
    data = {
        "corpAddressUniqueId": address_uid,
        "order": order_string,
        "tabUniqueId": tab['userTab']['uniqueId'],
        "targetTime": concat_target_time(tab),
        "userAddressUniqueId": address_uid,
    }
    return get_url("preorder/api/v2.1/orders/add?" + meican_params(data))

def cancle_order_url(tab, order_id):
    data = {
        "uniqueId": order_id,
        "type": "CORP_ORDER",
        "restoreCart": "false",
    }
    return get_url("preorder/api/v2.1/orders/delete?" + meican_params(data))

def restaurant_dishes_url(tab, restaurant_uid):
    data = {
        "restaurantUniqueId": restaurant_uid,
        "tabUniqueId": tab['userTab']['uniqueId'],
        "targetTime": concat_target_time(tab),
    }
    return get_url("preorder/api/v2.1/restaurants/show?" + meican_params(data))