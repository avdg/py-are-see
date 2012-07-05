import sys
import socket

from datetime import datetime

from src.settings import settings

class bot:
    def __init__(self):
        s = socket.socket()
        s.connect((settings["host"], settings["port"]))
        s.send("NICK %s\r\n" % settings["name"])
        s.send("USER %s %s bla :%s\r\n" % (settings["ident"], settings["host"], settings["realname"]))
        s.send("JOIN :%s\r\n" % settings["chan"])

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

if __name__ == "__main__":
    bot()