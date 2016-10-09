#!/usr/bin/python

import Api
import json, sys, ConfigParser, subprocess, socket, platform, os
from optparse import OptionParser

def main(myArgs):
    parser = OptionParser()
    parser.add_option("-b", help="server ip address")
    parser.add_option("-i", help="id")
    (options, args) = parser.parse_args()
    if options.i is None:
        parser.error(helper())
    nodeid = options.i
    if options.b is None:
        parser.error(helper())
    server = options.b

    serverStrip(server)

    cfg = ConfigParser.RawConfigParser()
    cfg.read('key.cfg')      
    key=dict(cfg.items("Keys"))
    for x in key:
        key[x]=key[x].split("#",1)[0].strip() 
    globals().update(key)  

    accessKey = accesskey
    secretKey = secretkey
    headerValue = {}

    nodeId = '/api/node/' + nodeid

    bassUrl = "http://" + server
    r = Api.REST(secretKey=secretKey, accessKey=accessKey, url=serverUrl)
    serverCheck(serverName, nodeId, headerValue, r, serverPort)
    
def serverCheck(serverName, nodeId, headerValue, r, serverPort):
    if platform.system() == "CYGWIN_NT-6.1":
        hiThere = "ping -n 1 " + serverName + " > /dev/null"
        if os.system(hiThere) == 0:
            socketCheck(serverName, serverPort)
            r.request('DELETE', nodeId, headers=headerValue)
        else:
            subprocess.call('clear', shell=True)
            print "Bad IP or Address for server: "  + serverName + " is completely unreachable"
            quit()
    else:
        hiThere = "ping -c 1 " + serverName + " > /dev/null"
        if os.system(hiThere) == 0:
            socketCheck(serverName, serverPort)
            r.request('DELETE', nodeId, headers=headerValue)
        else:
            subprocess.call('clear', shell=True)
            print "Bad IP or Address for server: " + serverName + " is completely unreachable"
            quit()

def socketCheck(serverName, serverPort):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    x = serverName + "," + serverPort
    x = x.split(",")
    x[1] = int(x[1])
    x = tuple(x)
    k = s.connect_ex(x)
    if k != 0:
        subprocess.call('clear', shell=True)
        print "The server IP/name: " + serverName +" is up however port "+ serverPort +" is not open."
        print '''
If unspecified this tool defaults to use https. 

If your server doesn't run on https then specify
a differant port explicitly in the server name. 

Example: 
(-b dorkcloud.com:80) rather than (-b dorkcloud.com)

        '''
        quit()
    else:
        s.close()

def serverStrip(server):
    global serverUrl
    global serverName
    global serverPort

    if ':' in server:
        serverPort=server.split(":", 1)[1].rstrip()
        serverName = server.split(":", 1)[0].rstrip()
    else:
        serverPort="443"
        serverName=server
        server = serverName + ":" + serverPort

    if serverPort == "443":
        serverUrl = "https://" + serverName

    elif serverPort == "80":
        serverUrl = "http://" + serverName

    else:
        serverUrl = "http://" + server
        
    print serverUrl

def helper():
    subprocess.call('clear', shell=True)
    print '''
This script is used to delete a particular node 


Usage: 
./node-delete.py -b <serverName-or-ipAddress> -i <node-id> 


Example: 
./node-delete.py -b dorkcloud.com -i 14 

 ### Please use the -h switch to list all the manditory switches for this command ### 

    '''

if __name__ == "__main__":
    main(sys.argv[1:])

