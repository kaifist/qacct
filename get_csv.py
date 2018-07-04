import qacct as qc
import cpu 
import du_user as du
import cpu_du as cd
import grupo_total as tg


# creamos el archivo qacct 
qacct = qc.Qacct()
qacct.b = qacct.date_numbers()
qacct.e = qacct.date_numbers()
#qacct.qacct()

# creamos el archivo uso de cpu
cpu_file = cpu.get_cpu(qacct.qacct())

# modificamos el archivo uso de disco
du_file = du.du("du_user_raw.txt")

# juntamos los dos archivos cpu y du
total_file = cd.cpu_du('total_cpu_du.txt', 'users_du.txt', 'cpu_file')

# creamos el archivo final
tg.by_group('total_cpu_du.txt', qacct.b, qacct.e)

