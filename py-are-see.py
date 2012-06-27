import sys
import socket

from datetime import datetime

host = "irc.freenode.org"
port = 6667
chan = "#udacity,##udacity-cs253"
name = "py-are-see"
ident = "py-are-see"
realname = "py-are-see"

s = socket.socket()
s.connect((host, port))
s.send("NICK %s\r\n" % name)
s.send("USER %s %s bla :%s\r\n" % (ident, host, realname))
s.send("JOIN :%s\r\n" % chan)

readbuffer = ""
while True:
    readbuffer = readbuffer+s.recv(1024)
    temp = readbuffer.split("\n")
    readbuffer = temp.pop( )

    for line in temp:
        line = line.rstrip().split()

        print datetime.now(), ' <- ', line

        if (line[0] == "PING"):
            print datetime.now(), ' -> PONG %s\r\n' % line[1]
            s.send("PONG %s\r\n" % line[1])