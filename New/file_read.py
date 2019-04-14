import time

f = open('/home/pi/text.txt', 'r')               # f is file descriptor
c=f.read()                                       # read the file using
print c[0],c[1],c[2],c[3],c[4]

