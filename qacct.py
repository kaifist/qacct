# -*- coding: utf-8 -*-
from __future__ import division
import os
import subprocess
import time
from datetime import date, datetime


class Qacct():
	''' run qacct and select the data user, cpu and mem in hours '''
	#def __init__(self, b='201601010000', e='201612312359', date = None, users = None):
	def __init__(self, b='', e='', date = None, users = None):
		self.b = b                                          # begin date
		self.e = e                                          # end date
		self.qfn = self.b[0:6] + '_' + self.e[0:6] + '.txt' # name for filename 
		self.date = time.strftime("%Y_%m_%d")               # actual date
		
	def date_numbers(self):
		''' "template" to change b and e. check date format
			before any change. 'check_date' works with INTRO too '''
		# TODO just two entries?? (date yyyymmdd and time HHMM)
		time = ''
		check_time = None 
		while check_time != 'y' and len(time) !=12:
			
			yy = raw_input('year from 2014: ')
			mm = raw_input('month 01-12: ')
			dd = raw_input('day 01-31: ')
			HH = raw_input('hour 00-23: ')
			MM = raw_input('minute 00-59: ')

			time = str(yy + mm + dd + HH + MM)
			print time
			check_time = str(raw_input('is it correct?(Y/N) '))
			if check_time == 'n' or check_time == 'N':
				continue
			try:
				time_asdate = datetime.strptime(time, '%Y%m%d%H%M') 
				
			except ValueError:
				print 'Hay algun error en el input: %s' % time
				print 'repite por favor'
				check_time = 'n'
		return time


	def qacct(self):
		'''run qacct and save the output in a file. 
		   user option -o activated by default '''
		qacct_fn = self.qfn #file name where output of qacct is saved
		with open(qacct_fn, 'w') as file:
			comando = ['qacct' + ' -b ' + self.b + ' -e ' + self.e + ' -o']
			print comando # visual check if comando it's ok
			subprocess.call(comando, shell=True, stdout=file)
		
		return qacct_fn


	
