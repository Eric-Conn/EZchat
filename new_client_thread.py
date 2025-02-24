import socket

import re

import time

import hashlib
import base64

gid = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"




def new_client_thread(client, address,dummy_update_response):

    print(f'CONNECTION WITH ADDRESS {address} OPENED.---------')
 

    #### This is where a new thread should be created.


    request_from_client = client.recv(1024).decode('utf-8')

    print(request_from_client)
    print('===============')

    print('CHECKING FOR HANDSHAKE... \n')



    handshake_check_regex_result = re.search('Sec-WebSocket-Key: ',request_from_client)

    if handshake_check_regex_result:

        start_of_key = handshake_check_regex_result.span()[1]
        # txt_pt2 = client_request[start_of_key:]
        rel_end_of_key = re.search('\r\n',request_from_client[start_of_key:]).span()[0]
        end_of_key = start_of_key + rel_end_of_key
        print('UPDATE KEY RECIEVED; KEY: \n')
        print(request_from_client[start_of_key:end_of_key])

        update_key = request_from_client[start_of_key:end_of_key]
        
        
        update_response_accept = base64.b64encode(\
            hashlib.sha1((update_key + gid).encode('utf-8')).digest())



        response_to_send = b'HTTP/1.1 101 Switching Protocols\r\n\
        Upgrade: websocket\r\n\
        Connection: Upgrade\r\n\
        Sec-WebSocket-Accept: ' + update_response_accept


        print('UPDATE RESPONSE:')






        print(update_response_accept.decode('utf-8'))
        client.send(response_to_send)

        




    else:
        print('NO UPDATE KEY RECIEVED')


    

    
    time.sleep(1)
    request_for_blast = client.recv(1024).decode('utf-8')
    print(request_for_blast)



    response_cap = 2
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
