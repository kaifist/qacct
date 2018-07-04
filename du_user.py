# -*- coding: utf-8 -*-
from __future__ import division
import os
import subprocess

# file_name = 'disk_usage.txt'

### get_du_user_raw_file
# # creamos un fichero con los consumos de cada usuario
# #with open(file_name, 'a') as file:
# #	for i in users_list:
# #		comando = ['cd /home/usuaris && du -sh ' + i]
# #		subprocess.call(comando, shell=True, stdout=file)
		
# # jugamos con el fichero


def du(du_raw_file):
	'''a partir del archivo du_file_raw calcula el precio 
       por uso de disco de cada usuario si es superior a 1G'''

	with open(du_raw_file) as file:

		disk_sp = 25
		precio_dsp = 1.16
		
		save_file = open("users_du.txt", "w")
		lines = file.readlines()
		for i in lines:
			line = i.split() # separo la linea en distintos elementos
			save_file.write(line[1] + '\t') # user
			save_file.write(line[0] + '\t')
			if 'G' in line[0]:
				save_file.write(str(float(line[0][0:-1])/disk_sp * precio_dsp))
				save_file.write('\n')
			elif 'T' in line[0]:
				save_file.write(str((float(line[0][0:-1])*1024)/disk_sp * precio_dsp))
				save_file.write('\n')
			else: save_file.write('0\n')
		save_file.close()



