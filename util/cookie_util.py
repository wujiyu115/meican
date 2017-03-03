# -*- coding: utf-8 -*-
# @Author: far
# @Date:   2017-02-26 21:55:58
# @Last Modified by:   wujiyu
# @Last Modified time: 2017-02-28 12:53:53
import requests.cookies
import os
import pickle
from util.configutil import ConfigUtil

def save_cookies(session, filename):
    with open(filename, 'w') as f:
        f.truncate()
        pickle.dump(session.cookies._cookies, f)
        return True


def load_cookies(session, filename):
    if not os.path.isfile(filename):
        return False

    with open(filename) as f:
        try:
            cookies = pickle.load(f)
            if cookies:
                jar = requests.cookies.RequestsCookieJar()
                jar._cookies = cookies
                session.cookies = jar
                return True
            else:
                return False
        except EOFError:
            return False

def has_cookies():
        return os.path.isfile(ConfigUtil.instance().cookies)