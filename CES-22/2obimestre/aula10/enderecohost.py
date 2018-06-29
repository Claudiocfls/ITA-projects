
# [EXEMPLO]

import socket
def get_remote_machine_info():
	remote = 'www.ita.br'
	print("ip address: %s" % socket.gethostbyname(remote))
def print_machine_info():
	host_name = socket.gethostname()
	ip_add = socket.gethostbyname(host_name)
	print("host name: %s" % host_name)
	print('ip add: %s' % ip_add)
if __name__ == '__main__':
	print_machine_info()
	get_remote_machine_info()