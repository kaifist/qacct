def get_cpu(txt):
	''' delete two first lines from qacct file.
	select columns [0] user, [4] cpu and calculate cpu/h and cost.
	save the output in a file (actual_date-qacct_date)'''
        
#	qacct_fn = self.qfn
	with open(txt) as file:
		lines = file.readlines() 
		lines.pop(0) 
		lines.pop(0) # delete two first lines
		
		name_cpu_mem = []
		
		for i in range(0, len(lines)):
			a_line = lines[i].split()
                # 300 h/cpu = 2,77 euros
		# float to div, round to get a correct int, and then str again to save it
			name_cpu_mem.append('{0:<30}{1:<10}{2:<10}'.format(a_line[0],		   # user 
						str(int(round(float(a_line[4])/3600))),		   # cpu/h
						str(int(((round(float(a_line[4])/3600)/300*2.77))))# euros
						)
						) 
			
		save_file = 'cpu_file' 
		with open(save_file, 'w') as file:
			for i in range(0, len(name_cpu_mem)):
			 	file.write(''.join(name_cpu_mem[i]))
				file.write('\n')
		
		return save_file
