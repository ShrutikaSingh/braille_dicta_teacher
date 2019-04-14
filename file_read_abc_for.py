import time

f = open('/home/pi/textabc.txt', 'r')               # f is file descriptor
c=f.read()# read the file using
for i in range(0,26):
    if c[i] == 'a':
        print c[i] 
        time.sleep(1)
    if c[i] == 'b':
        print c[i]
        time.sleep(1)










