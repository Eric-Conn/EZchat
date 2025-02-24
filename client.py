import socket
import time
import queue

##### Dummy request

dummy_request = b"GET /chat HTTP/1.1\r\n\
Host: example.com:8000\r\n\
Upgrade: websocket\r\n\
Connection: Upgrade\r\n\
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n\
Sec-WebSocket-Version: 13\r\n\r\n"




"""258EAFA5-E914-47DA-
   95CA-C5AB0DC85B11"""



message_queue = queue.Queue(1)




#######



HOST = '192.168.1.48'

# HOST = '127.0.0.1'

# HOST = '127.0.0.1'
PORT  = 9090

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#targeting endpoint on server
client_socket.connect((HOST,PORT))


input('HIT ENTER TO SEND UPDATE KEY')
# client_socket.send('Blast Requested'.encode('utf-8'))
client_socket.send(dummy_request)

update_response_from_server = client_socket.recv(1024)

print('+++++++++++++START update key response\n')

print(update_response_from_server)


print('+++++++++++++END update key response\n')

client_socket.send('request_for_blast = True'.encode('utf-8'))

print("waiting for blast---")
# for i in range(10):
#     print(i,'\r')
#     time.sleep(1)




# input('HIT ENTER TO RECIEVE BLAST')
print('START Recieve Blast')
while True:
    
    print('>',client_socket.recv(1024).decode('utf-8'),'\n')

    if len(client_socket.recv(1024)) == 0:
        break


print('END Recieve Blast; zero bytes recieved')

