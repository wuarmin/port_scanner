import socket
import termcolor



def scan(target, ports):
	print('\n' + 'starting scan for target ' + str(target))
	for port in range(1, ports):
		scan_port(target, port)



def scan_port(ip_addr, port):
	try:
		sock = socket.socket()
		sock.connect((ip_addr, port))
		print('[+] port opened ' + str(port))
		sock.close()
	except:
		pass




target = input('[*] enter target to scan (splitted by \',\'): ')
ports = int(input('[*] enter how many ports you want to scan: '))

if ',' in target:
	print(termcolor.colored('[*] scanning multiple targets', 'green'))
	for target in target.split(','):
		ip_addr = target.strip(' ')
		scan(ip_addr, ports)
else:
	scan(target, ports)
