#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os
import errno
import time

def mkdir_p(path):
	"""http://stackoverflow.com/a/600612/190597 (tzot)"""
	try:
		os.makedirs(path, exist_ok=True)  # Python>3.2
	except TypeError:
		try:
			os.makedirs(path)
		except OSError as exc: # Python >2.5
			if exc.errno == errno.EEXIST and os.path.isdir(path):
				pass
			else: raise

class MakeFileHandler(logging.handlers.TimedRotatingFileHandler):
	def __init__(self,filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False):            
		mkdir_p(os.path.dirname(filename))
		log_path =os.path.splitext(filename)
		log_file = '%s-%s%s'%(log_path[0],time.strftime("%Y-%m-%d", time.localtime()), log_path[1])
		logging.handlers.TimedRotatingFileHandler.__init__(self, log_file, when, interval, backupCount, encoding, delay, utc)
		# logging.handlers.TimedRotatingFileHandler.__init__(self, filename, when, interval, backupCount, encoding, delay, utc)
