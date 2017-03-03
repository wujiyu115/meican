#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from util.mylog import *

class UnicodeStreamFilter:

	def __init__(self, target):
		self.target = target
		self.encoding = 'utf-8'
		self.errors = 'replace'
		self.encode_to = self.target.encoding

	def write(self, s):
		if type(s) == str:
			s = s.decode('utf-8')
		s = s.encode(self.encode_to, self.errors).decode(self.encode_to)
		self.target.write(s)

	def flush(self):
		self.target.flush()

def stdout_encoding():
	if sys.stdout.encoding == 'cp936':
		sys.stdout = UnicodeStreamFilter(sys.stdout)

def trans2utf8( data):
	if not data:
		return data
	result = None
	if type(data) == unicode:
		result = data
	elif type(data) == str:
		result = data.decode('utf-8')
	return result

def decode_listutf8(data):
	rv = []
	for item in data:
		if isinstance(item, unicode):
			item = item.encode('utf-8')
		elif isinstance(item, list):
			item = decode_listutf8(item)
		elif isinstance(item, dict):
			item = decode_dictutf8(item)
		rv.append(item)
	return rv


def decode_dictutf8(data):
	rv = {}
	for key, value in data.iteritems():
		if isinstance(key, unicode):
			key = key.encode('utf-8')
		if isinstance(value, unicode):
			value = value.encode('utf-8')
		elif isinstance(value, list):
			value = decode_listutf8(value)
		elif isinstance(value, dict):
			value = decode_dictutf8(value)
		rv[key] = value
	return rv