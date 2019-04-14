import socket


sock = socket.socket()
sock.bind(('192.168.0.120', 8009))
sock.listen(5)
client, adress = sock.accept()

print "Incoming:", adress
print client.recv(1024)
print

client.send('HTTP/1.0 200 OK\r\n')
client.send("Content-Type: text/html\r\n\r\n")
client.send('<html><body><h1>Hello World</body></html>')
client.close()

print "Answering ..."
print "Finished."

sock.close()
