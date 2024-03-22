# A Simple Web Browser Requesting via Socket.
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n".encode()   #Encode request from Unicode to UTF-8 and assignment
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")   # Decode response from UTF-8 to Unicode and print

mysock.close()