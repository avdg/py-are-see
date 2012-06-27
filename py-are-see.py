import sys
import socket

host = "irc.freenode.org"
port = 6667
chan = "#udacity"
name = "py-are-see"
ident = "py-are-see"
realname = "py-are-see"

s = socket.socket()
s.connect((host, port))
s.send("NICK %s\r\n" % name)
s.send("USER %s %s bla :%s\r\n" % (ident, host, realname))
s.send("JOIN :%s\r\n" % chan)

readbuffer = ""
while 1:
    readbuffer = readbuffer+s.recv(1024)
    temp = readbuffer.split("\n")
    readbuffer = temp.pop( )

    for line in temp:
        line = line.rstrip().split()

        if (line[0] == "PING"):
            s.send("PONG %s\r\n" % line[1])