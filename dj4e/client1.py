# A Simple Web Client.
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creating a socket for our client.
mysock.connect(("localhost", 9000))
cmd = "GET http://localhost/ HTTP/1.0\r\n\r\n".encode()   #Encode request from Unicode to UTF-8 and assignment
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")   # Decode response from UTF-8 to Unicode and print

mysock.close()

