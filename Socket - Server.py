print("-------------------------------------------\nNauman - 648\n-------------------------------------------")
import socket

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()

port=9999

serversocket.connect((host,port))

tm=serversocket.recv(1024)
serversocket.close()
print("The time got from the server is %s"%tm.decode('ascii'))
