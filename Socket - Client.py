print("-------------------------------------------\nNauman - 648\n-------------------------------------------")
import time
import socket

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()

port=9999

serversocket.bind((host,port))

serversocket.listen(5)

while True:
  clientsocket,addr=serversocket.accept()
  print("Got a Connection from %s"%str(addr))
  currentTime=time.ctime(time.time())+"\r\n"
  clientsocket.send(currentTime.encode('ascii'))
  clientsocket.close()
