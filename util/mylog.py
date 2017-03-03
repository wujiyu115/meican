#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
import logging
import logging.handlers
import logging.config
import yaml
import traceback
import time

from util.codecutil import stdout_encoding
from configutil import ConfigUtil
import colorama
from colorama import Fore, Back, Style

LEVEL_INFO ="info"
LEVEL_DEBUG ="debug"
LEVEL_WARNING ="warn"
LEVEL_ERROR ="error"
LEVEL_CRITICAL ="critical"


def __log(level_func, message, logger_name):
	try:
		logger = logging.getLogger(logger_name)
		getattr(logger, level_func)(message)
	except:
		print(traceback.format_exc())
		pass

def color_info(message, logger_name = "root"):
	__log(LEVEL_INFO, '%s%s%s'%(Fore.GREEN, message, Fore.RESET), logger_name)

def color_debug(message, logger_name = "root"):
	__log(LEVEL_DEBUG, '%s%s%s'%(Fore.CYAN, message, Fore.RESET), logger_name)

def color_warn(message, logger_name = "root"):
	__log(LEVEL_WARNING, '%s%s%s'%(Fore.YELLOW, message, Fore.RESET), logger_name)

def color_error(message, logger_name = "root"):
	__log(LEVEL_ERROR, '%s%s%s'%(Fore.RED, message, Fore.RESET), logger_name)

def color_critical(message, logger_name = "root"):
	__log(LEVEL_CRITICAL, '%s%s%s'%(Fore.MAGENTA, message, Fore.RESET), logger_name)

########################interface#######################################
def info(message, logger_name = "root"):
	color_info(message, logger_name)

def debug(message, logger_name = "root"):
	color_debug(message, logger_name)

def warn(message, logger_name = "root"):
	color_warn(message, logger_name)

def error(message, logger_name = "root"):
	color_error(message, logger_name)

def critical(message, logger_name = "root"):
	color_critical(message, logger_name)

def blank(logger_name = "root"):
	__log(LEVEL_INFO, '', logger_name)


def install_log():
	colorama.init()
	logger = logging.getLogger()
	log_level =   str(ConfigUtil.instance().log_level if hasattr(ConfigUtil.instance(),"log_level") else "INFO")
	# 分割log
	if sys.hexversion>0x20700f0:
		logging.config.dictConfig(yaml.load(open(ConfigUtil.instance().loggingyaml, 'r')))
	else:
		log_file = 'logging.%s-%d.log'%(time.strftime("%Y-%m-%d--%H-%M-%S", time.localtime()), os.getpid())
		timelog = logging.handlers.TimedRotatingFileHandler(log_file,'midnight', 1, 0)
		logger.addHandler(timelog)
	logging.config.dictConfig(yaml.load(open(ConfigUtil.instance().loggingyaml, 'r')))
	logger.setLevel(log_level)

	stdout_encoding()

