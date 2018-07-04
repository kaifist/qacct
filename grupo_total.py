# -*- coding: utf-8 -*-

def by_group(total_file, desde, hasta):

	groups = None # due confidentiality I can't show users
                      # this is a dict where keys are the groups and values
                      # are the user corresponding to the group
        
	''' create a new file with the users separated by research group'''
	#self.read_data()
		
	#data = self.date + '-' + self.qfn #'04_10_2017-201601_201706.txt'

	eiac = []
	embm = []
	etyc = []
	admn = []
	othr = []

	with open(total_file) as file:
		for line in file:
		#print [line if line.split()[0] in grupos.values()[i] else others.append(line) for i in range(len(grupos)) ]
			if line.split()[0] in groups['Ecologia Integrativa de Aguas Continentales']:
				eiac.append(line)
			elif line.split()[0] in groups['Ecologia Molecular del Bentos Marino']:
				embm.append(line)
			elif line.split()[0] in groups['Ecologia Teorica y Computacional']:
				etyc.append(line)
			elif line.split()[0] in groups['Admins']:
				admn.append(line)
			else: othr.append(line)
		
		

	to_save = 'consumo_disco_y_cpu_' + str(desde)[0:8] + '_' + str(hasta)[0:8] + '.csv' #+ qc.qfn
	with open(to_save, 'w') as file:
		#file.write('comando: ' + self.b + '\t' + self.e+'\n\n')
		file.write('\tuser\tdisk\t€/disk\tcpu\t€/cpu\ttotal\n')
		file.write('-Ecologia Integrativa de Aguas Continentales\n\n')
		for i in eiac:
			file.write('\t'+i)
		file.write('\n-Ecologia Molecular del Bentos Marino\n\n')
		for i in embm:
			file.write('\t'+i)
		file.write('\n-Ecologia Teorica y Computacional\n\n')
		for i in etyc:
			file.write('\t'+i)
		file.write('\n-Admins\n\n')
		for i in admn:
			file.write('\t'+i)
		file.write('\n-Others\n\n')
		for i in othr:
			file.write('\t'+i)



		
