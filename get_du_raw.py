# -*- coding: utf-8 -*-
from __future__ import division
import os
import subprocess

''' Genera una lista de los usuarios de /home/usuaris'''
# lista de usuarios

with open('users_list.txt', 'w') as us_file:
	cm = ['ls /home/usuaris/.']
	subprocess.call(cm, shell=True, stdout=us_file)


## get_du_user_raw_file
# creamos un fichero con los consumos de cada usuario
with open(file_name, 'w') as file:
	for i in users_list:
		comando = ['cd /home/usuaris && du -sh ' + i]
		subprocess.call(comando, shell=True, stdout=file)



with open('users_list.txt', 'w') as us_file:
     cm = ['ls /home/usuaris/.']
     subprocess.call(cm, shell=True, stdout=us_file)
 
file_name = 'users_list.txt'

## get_du_user_raw_file
# creamos un fichero con los consumos de cada usuario
with open(file_name) as file:
	to_save_in = open('du_user_raw.txt', 'a')
	for i in file:
		comando = ['cd /home/usuaris && du -sh ' + i]
		subprocess.call(comando, shell=True, stdout=to_save_in)
	to_save_in.close()
