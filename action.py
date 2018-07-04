#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import sys,os
import inspect
import Worker as words
import time

pathapp = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(pathapp + "/config")

reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
sys.stdin = codecs.getreader('utf_8')(sys.stdin)

import Environment as env

if __name__ == '__main__':
	argNames = ['command', 'task']
	args = dict(zip(argNames, sys.argv))

	tasks = ['sendqueue', 'progressqueue']

	if 'task' not in args:
		print('===> Not found task in tasks')
		for vtask in tasks:
			print('- ' + vtask)
		exit()
	
	task = args['task']
	if task in tasks:

		# words.Worker().sendqueue()

		method_to_call = getattr(words.Worker(), task)
		if task=='sendqueue':
			import daemon 
			with daemon.DaemonContext():
				while True:
					method_to_call()
					#time.sleep(env.INTERVAL-14)
					time.sleep(env.INTERVAL*60)
		else:
			method_to_call()
	else:
		print('===> Not found task in tasks')
		for vtask in tasks:
			print('- ' + vtask)
		exit()
