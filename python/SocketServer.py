import socket
import sys
import signal
from thread import *

#**********************************************************************
def signal_handler(signal, frame):
        print('')
        s.close()
        sys.exit(0)

# Register a handler of <CTRL+C> to stop the server
signal.signal(signal.SIGINT, signal_handler)

#**********************************************************************
HOST = ''           # Symbolic name meaning all available interfaces
PORT = 5001         # Arbitrary non-privileged port
RECV_BUFF = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print 'Socket created'
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
print 'Socket bind complete'

s.listen(10)
print 'Socket now listening'


#**********************************************************************
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    with open('received_file', 'wb') as f:
        print 'File opened'
        while True:
            data = conn.recv(RECV_BUFF)
            if not data:
                break
            #print(data)
            #print('')
            # write data to a file
            f.write(data)
    f.close()
    print('Successfully get the file')
     
    #came out of loop
    conn.close()
    
#**********************************************************************
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    conn.settimeout(60)
    
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
    
s.close()
