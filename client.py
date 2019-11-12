#import libraries
import socket
import time
import sys

print('Client Server...')
time.sleep(1)
#Create an socket object
try: 
   s = socket.socket()
   print ('Socket successfully created')
except socket.error as err: 
   print ('socket creation failed with error %s' %(err))
 
#Get the hostname, IP Address from socket and set Port
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
#get information to connect with the server
print(host_name, '({})'.format(ip))
server_host = ip ##input('Enter server\'s IP address:')
name = input('Enter Client\'s name: ')
port = 1234
print('Trying to connect to the server: {}, ({})'.format(server_host, port))
time.sleep(1)
#connecting to the server
s.connect((server_host, port))
print('Connected...\n')
s.send(name.encode())
server_name = s.recv(1024)
server_name = server_name.decode()
print('{} has joined...'.format(server_name))
print('Enter \'bye\' to exit.')
while True:
   message = s.recv(1024)
   message = message.decode()
   print(server_name, '>', message)
   message = input(str('Me > '))
   if message == 'bye':
      message = 'Leaving the Chat.'
      s.send(message.encode())
      print('\n')
      break
   s.send(message.encode())