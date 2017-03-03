# -*- coding: utf-8 -*-
# @Author: wujiyu
# @Date:   2016-11-23 18:25:06
# @Last Modified by:   wujiyu
# @Last Modified time: 2016-11-24 14:23:49

from configutil import ConfigUtil

def is_debug():
    return ConfigUtil.instance().log_level == "DEBUG"