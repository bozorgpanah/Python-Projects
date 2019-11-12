#first of all import libraries 
import socket
import time
import sys

print('Setup Server...')
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
port = 1234
s.bind((host_name, port))
print(host_name, '({})'.format(ip))
name = input('Enter server\'s name: ')
#put the socket into listening mode 
s.listen(1) 
print('Waiting for incoming connections...')
#establish connection with client
connection, addr = s.accept()
print('Received connection from ', addr[0], '(', addr[1], ')\n')
print('Connection Established. Connected From: {}, ({})'.format(addr[0], addr[0]))
#get a connection from client side
client_name = connection.recv(1024)
client_name = client_name.decode()
print(client_name + ' has connected.')
print('Press \'bye\' to leave chat!')
#send a message to the client
connection.send(name.encode())
while True:
   message = input('Me > ')
   if message == 'bye':
      message = 'Have a nice day, bye.'
      connection.send(message.encode())
      print('\n')
      break
   connection.send(message.encode())
   message = connection.recv(1024)
   message = message.decode()
   print(client_name, '>', message)