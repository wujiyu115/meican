# -*- coding: utf-8 -*-

import datetime
import time as time_
import json
import os

def milli_to_datetime(milliseconds):
    return datetime.date(1970, 1, 1) + datetime.timedelta(milliseconds=int(milliseconds))

def milli_strftime(milliseconds, format = '%Y-%m-%d'):
    return milli_to_datetime(milliseconds).strftime(format)

def millis():
    return int(round(time_.time() * 1000))

def empty_list(list):
    return list is None or len(list) == 0

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')
