def cpu_du(total_file_name, du_file_name, cpu_file_name):
	'''une los dos archivos, du y cpu en uno y crea la columna de los totales'''
	with open(total_file_name, 'w') as file3:
		cpu_file = open(cpu_file_name)
		du_file = open(du_file_name)
		cpu = cpu_file.readlines()
		du = du_file.readlines()
		line_total = []

		for i in du:
			line_du = i.split()
			for j in cpu:
				line_cpu = j.split()
				if line_cpu[0] == line_du[0]:
					line_du.append(line_cpu[1])
					line_du.append(line_cpu[2])
					line_total.append(line_du)
	
			if line_du not in line_total:
				line_total.append(line_du)
		for i in line_total:
			if len(i) > 3:
				file3.write(' '.join(i))
				suma = (float(i[2])+float(i[4]))
				file3.write(' ' + str(suma) + '\n')
			else:
				file3.write(' '.join(i) + '\n')

