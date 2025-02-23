import socket

import re


HOST = '192.168.1.48'

# HOST = '127.0.0.1'

PORT  = 9090


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((HOST,PORT))

print('SERVER ONLINE')
print(f'LISTENING AT PORT {HOST}:{PORT}')

server.listen(1)


while True:

    client, address = server.accept()
    
    print(f'CONNECTION WITH ADDRESS {address} OPENED.---------')
 

    ###### This is where a new thread should be created.

    request_from_client = client.recv(1024).decode('utf-8')

    print(request_from_client)
    print('===============')


    response_cap = 10
    k = 0

########test start


    while k < response_cap:


        #I need the right prtocol that chrome will be using

        #What type of server will the browser be?

        #A ws server? how does ws worK?

        to_send = f'response {k+1}/{response_cap}\n'

        client.send(b'HTTP/1.0 200 OK\r\n'  \
        + b'Content-Type: text/html\r\n\r\n'+ to_send.encode('utf-8'))

        k+=1

    

    client.close()
    
    print(f'CONNECTION WITH ADDRESS {address} CLOSED.---------')

########test end


    if re.search('GET /recieve_blast',request_from_client):

        #Get upgrade header
        #if re.search(dsds):

        # send upgrade response


        #The start ws connection




        
        while k < response_cap:



            #I need the right prtocol that chrome will be using

            #What type of server will the browser be?

            #A ws server? how does ws worK?

            to_send = f'response {k+1}/{response_cap}\n'

            client.send(b'HTTP/1.0 200 OK\r\n'  \
            + b'Content-Type: text/html\r\n\r\n'+ to_send.encode('utf-8'))

            k+=1

        

        client.close()
        print(f'CONNECTION WITH ADDRESS {address} CLOSED.---------')

        















