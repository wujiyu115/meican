#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wujiyu
# @Date:   2016-03-15 20:43:04
# @Last Modified by:   wujiyu
# @Last Modified time: 2017-03-24 10:36:26
import threading
import os,ConfigParser
import pprint
from util.obj_util import obj_dict
import codecs

class ConfigUtil(object):
    _instance_lock = threading.Lock()

    @staticmethod
    def instance():
        if not hasattr(ConfigUtil, "_instance"):
            with ConfigUtil._instance_lock:
                if not hasattr(ConfigUtil, "_instance"):
                    ConfigUtil._instance = ConfigUtil()
        return ConfigUtil._instance


    def __init__(self):
        pass

    def setConfigFile(self,fixed_config_file="cfg/config.conf"):
        self.fixed_config_file = fixed_config_file
        fixed_config = ConfigParser.ConfigParser()
        fixed_config.readfp(codecs.open(fixed_config_file, "r", "utf-8"))
        # fixed_config.read(fixed_config_file)

        for section in fixed_config.sections():
            for p, value in fixed_config.items(section):
                if value.isdigit():
                    setattr(self,p,int(value))
                else:
                    if value=="true" or value=="false" :
                        setattr(self,p,fixed_config.getboolean(section,p))
                    else:
                        vt = value.strip().split(",")
                        if len(vt) > 1:
                            setattr(self,p,vt)
                        else:
                            setattr(self,p,vt[0])
        if self.is_debug():
            pprint.pprint(obj_dict(self,["_instance_lock","_instance"]),width=4)

    def is_debug(self):
        return self.log_level =="DEBUG"

ConfigUtil.instance().setConfigFile()
