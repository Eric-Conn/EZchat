import socket

import re

import threading

from new_client_thread import new_client_thread


dummy_update_response = "HTTP/1.1 101 Switching Protocols\
Upgrade: websocket\
Connection: Upgrade\
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo="



HOST = '192.168.1.48'

# HOST = '127.0.0.1'

PORT  = 9090


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((HOST,PORT))

print('SERVER ONLINE')
print(f'LISTENING AT PORT {HOST}:{PORT}')

server.listen(2)


print('INITIAL THREADS ON SERVER: \n')
print(threading.enumerate())



while True:

    

    client, address = server.accept()

    



    # new_client_thread(client, address,dummy_update_response)



    threading.Thread(target = new_client_thread,\
        args = (client, address,dummy_update_response) \
             ,daemon=True).start()


    print('===NEW THREAD MADE===')
    print('CURRENT THREADS ON SERVER: \n')
    print(threading.enumerate())

    


#     print(f'CONNECTION WITH ADDRESS {address} OPENED.---------')
 

#     #### This is where a new thread should be created.


#     request_from_client = client.recv(1024).decode('utf-8')

#     print(request_from_client)
#     print('===============')

#     print('CHECKING FOR HANDSHAKE... \n')



#     handshake_check_regex_result = re.search('Sec-WebSocket-Key: ',request_from_client)

#     if handshake_check_regex_result:

#         start_of_key = handshake_check_regex_result.span()[1]
#         # txt_pt2 = client_request[start_of_key:]
#         rel_end_of_key = re.search('\r\n',request_from_client[start_of_key:]).span()[0]
#         end_of_key = start_of_key + rel_end_of_key
#         print('UPDATE KEY RECIEVED; KEY: \n')
#         print(request_from_client[start_of_key:end_of_key])


#         client.send(dummy_update_response.encode('utf-8'))
        




#     else:
#         print('NO UPDATE KEY RECIEVED')

    





#     response_cap = 2
#     k = 0

# ########test start


#     while k < response_cap:


#         #I need the right prtocol that chrome will be using

#         #What type of server will the browser be?

#         #A ws server? how does ws worK?

#         to_send = f'response {k+1}/{response_cap}\n'

#         client.send(b'HTTP/1.0 200 OK\r\n'  \
#         + b'Content-Type: text/html\r\n\r\n'+ to_send.encode('utf-8'))

#         k+=1

    

#     client.close()
    
#     print(f'CONNECTION WITH ADDRESS {address} CLOSED.---------')

# ########test end


    # if re.search('GET /recieve_blast',request_from_client):

    #     #Get upgrade header
    #     #if re.search(dsds):

    #     # send upgrade response


    #     #The start ws connection




        
    #     while k < response_cap:



    #         #I need the right prtocol that chrome will be using

    #         #What type of server will the browser be?

    #         #A ws server? how does ws worK?

    #         to_send = f'response {k+1}/{response_cap}\n'

    #         client.send(b'HTTP/1.0 200 OK\r\n'  \
    #         + b'Content-Type: text/html\r\n\r\n'+ to_send.encode('utf-8'))

    #         k+=1

        

    #     client.close()
    #     print(f'CONNECTION WITH ADDRESS {address} CLOSED.---------')

        















