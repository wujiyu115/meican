# -*- coding:utf-8 -*-
import os
import errno
import json


class FileUtil:
	def __init__(self):
		pass

	@staticmethod
	def read(path,encode='UTF-8'):
		try:
			files = open(path,"r")
			strs= files.read()
			strs = strs.encode(encode)
			files.close()
			return strs
		except IOError,e:
			if e.errno==errno.ENOENT:
				return False
		return False

	@staticmethod
	def read_json(path):
		content =FileUtil.read(path)
		jobject = {}
		if content:
			jobject = json.loads(content)
		return jobject
		pass

	@staticmethod
	def write(path,content):
		FileUtil.mkdir_p(os.path.dirname(path))
		f = open(path, 'w+')
		f.write(content)
		f.close()
		pass

	@staticmethod
	def write_json(path,json_object):
		jstr = json.dumps(json_object)
		FileUtil.write(path,jstr)
		pass

	@staticmethod
	def get_dirs_files(dir_name):
		all_files = []
		for parent, dirnames, filenames in os.walk(dir_name):
			for filename in filenames:
				full_filename = os.path.join(parent, filename)
				all_files.append(full_filename)
		return all_files

	@staticmethod
	def mkdir_p(filename):
		folder=os.path.dirname(filename)
		try:
			if not os.path.exists(folder):
				os.makedirs(folder, exist_ok=True)  # Python>3.2
		except TypeError:
			try:
				if not os.path.exists(folder):
					os.makedirs(folder)
			except OSError as exc: # Python >2.5
				if exc.errno == errno.EEXIST and os.path.isdir(folder):
					pass
				else: raise

	@staticmethod
	def exist(file):
		return os.path.exists(file)