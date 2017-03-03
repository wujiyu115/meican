# -*- coding: utf-8 -*-
# @Author: far
# @Date:   2017-02-26 20:37:52
# @Last Modified by:   wujiyu
# @Last Modified time: 2017-02-28 11:22:52

errcode  = type('new', (object,), {})
desc = {}

errcode.ok = 0
desc[errcode.ok] = "成功"
errcode.wrong_user = 1
desc[errcode.wrong_user] = "登录用户名或者密码错误"
errcode.not_avilable_tabs = 2
desc[errcode.not_avilable_tabs] = "没有可订餐日期"
errcode.not_right_time_tabs = 3
desc[errcode.not_right_time_tabs] = "当前时间大于订餐日期"
errcode.not_index_tabs = 4
desc[errcode.not_index_tabs] = "订餐项大于当前可订项"
errcode.not_recommend = 5
desc[errcode.not_recommend] = "没有推荐菜品"
errcode.not_filter_recommend = 6
desc[errcode.not_filter_recommend] = "筛选后没有合适的推荐菜品"
errcode.money_dish_error = 7
desc[errcode.money_dish_error] = "没有找到合适价格的菜品"
errcode.order_error = 8
desc[errcode.order_error] = "订餐失败"
