import socket

HOST = '192.168.1.48'

# HOST = '127.0.0.1'

# HOST = '127.0.0.1'
PORT  = 9090

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#targeting endpoint on server
client_socket.connect((HOST,PORT))


input('HIT ENTER TO RECIEVE BLAST')
client_socket.send('Blast Requested'.encode('utf-8'))


print('START Recieve Blast')
while True:

    print('>',client_socket.recv(1024).decode('utf-8'),'\n')

    if len(client_socket.recv(1024)) == 0:
        break


print('END Recieve Blast; zero bytes recieved')

