#!/usr/bin/env python3
import sys
import os
from socket import AF_INET, SOCK_DGRAM, socket

SERVER = ("127.0.0.1", 20001)
BUFFERSIZE  = 1024

def cmd_serve():
    SS = socket(family=AF_INET, type=SOCK_DGRAM)
    SS.bind(SERVER)
    print("UDP server up and listening")
    while True:
        cmdB, client = SS.recvfrom(BUFFERSIZE)
        cmd = str(cmdB, 'utf-8')
        print('command: %s' % repr(cmd))
        if cmd == "--kill":
            print( "Server Killed" )
            return
        else:
            os.system(cmd + ' &')
            response = "OK"
            SS.sendto(str.encode(response), client)

def cmd_send(cmd):
    cmdB =str.encode(cmd)
    ss = socket(family=AF_INET, type=SOCK_DGRAM)
    ss.sendto(cmdB, SERVER)

def main():
    args=sys.argv[1:] or ['']
    subcommand = args.pop(0)
    if False: pass
    elif subcommand == 'start-server': cmd_serve()
    elif subcommand == 'stop-server': cmd_send( '--kill' )
    elif subcommand == 'send': cmd_send( ' '.join(args) )
    else: usage()

def usage():
    sys.stderr.write("""
USAGE:
    bchrpc SUBCOMMAND [ARGS]

SUBCOMMANDS:
    start-server  -- start server
    stop-server   -- stop server
    send          -- send [ARGS] to server
""")
