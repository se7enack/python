#!/usr/bin/python

import Api
import json, sys, ConfigParser, subprocess, socket, platform, os
from optparse import OptionParser

def helper():
    subprocess.call('clear', shell=True)
    print '''
This script lists server status 

Usage:
    ./server-status.py -b <serverName-or-ipAddr> 


Example: 
    ./server-status.py -b staging-dorkcloud.com

    '''

def main(myArgs):
    parser = OptionParser()
    parser.add_option("-b", help="server ip address")
    (options, args) = parser.parse_args()
    
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

    r = Api.REST(secretKey=secretKey, accessKey=accessKey, url=serverUrl)

    headerValue = {}
    headerValue["Accept"] = 'application/json' 
    headerValue["Content-Type"] = 'application/json'
    serverCheck(serverName, headerValue, r, serverPort)
    
def serverCheck(serverName, headerValue, r, serverPort):
    if platform.system() == "CYGWIN_NT-6.1":
        hiThere = "ping -n 1 " + serverName + " > /dev/null"
        if os.system(hiThere) == 0:
            socketCheck(serverName, serverPort)
            prJson(r.request('GET', '/api/status', headers=headerValue))
        else:
            subprocess.call('clear', shell=True)
            print "Bad IP or Address for server: "  + serverName + " is completely unreachable"
            quit()
    else:
        hiThere = "ping -c 1 " + serverName + " > /dev/null"
        if os.system(hiThere) == 0:
            socketCheck(serverName, serverPort)
            prJson(r.request('GET', '/api/status', headers=headerValue))
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
(-b staging-dorkcloud.com:80) rather than (-b staging-dorkcloud.com)

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

def prJson(data, indent=3):
    print json.dumps(data, indent=indent)


if __name__ == "__main__":
    main(sys.argv[1:])
