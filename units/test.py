# -*- coding: utf-8 -*-
import sys


# sys.path.append("../")

# from src.meican import MeiCan
# from util.obj_util import dict_obj, dict_item_obj
# from util.file_util import FileUtil
# import json
# from util.json_util import json_dump
# from urllib import urlencode
# import urllib

# dis_list =  FileUtil.read_json("stat/calendarItems.js")
# # ls = dict_item_obj(dis_list['myRegularDishList'])

# def available_tabs(self):
#     tabs = reduce(lambda x, y: x + y, [filter(lambda x: x['status'] == 'AVAILABLE', _['calendarItemList'])
#                                        for _ in dis_list['dateList']])


# person = raw_input('[Enter your email]: ')
# print('Hello', person)
# person = raw_input('[Enter your password]: ')
# print('password', person)

# from apscheduler.schedulers.background import BackgroundScheduler
# def mainjob():
#     print("It works!")

# if __name__ == '__main__':
#     sched = BackgroundScheduler()
#     sched.start()
#     sched.add_job(mainjob, 'interval', seconds=5)
#     raw_input("Press enter to exit.")
#     sched.shutdown()


# import schedule
# import time
# import functools
# import requests
# import traceback
# import datetime

# def catch_exceptions(job_func, cancel_on_failure=False):
#     @functools.wraps(job_func)
#     def wrapper(*args, **kwargs):
#         try:
#             return job_func(*args, **kwargs)
#         except:
#             import traceback
#             print(traceback.format_exc())
#             if cancel_on_failure:
#                 return schedule.CancelJob
#     return wrapper

# def job(t):
#     try:
#         print("do job <%s>"%datetime.datetime.now())
#         print(1/0)
#         c = requests.Session().get("http://www.baidu.com")
#         print("I'm working...<%s>"%len(c.content))
#     except Exception as e:
#         print(traceback.format_exc())

# schedule.every(2).seconds.do(job,"1")

# while True:
#     schedule.run_pending()
#     print("sleep111")
#     time.sleep(1)

# 这些目录里面的py文件都会被编译
cp_py = ["src", "util", "main.py"]
# 这些目录直接复制整个目录
cp_dirs = cp_py + ["cfg", "py", "README.md"]

import compileall
print(compileall.compilea)