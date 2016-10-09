#!/usr/bin/python

import Api
import json, sys, ConfigParser, subprocess, os, socket, platform
from optparse import OptionParser

def main(myArgs):
#manditory
    parser = OptionParser()
    parser.add_option("-b", help="server ip address")
    parser.add_option("-i", help="id")
#optional
    parser.add_option("-p", help="password")
    parser.add_option("-a", help="address")
    parser.add_option("-t", help="tier")
    parser.add_option("-f", help="friendly")
    parser.add_option("-s", help="content")
    parser.add_option("-n", help="accountNumber")
    parser.add_option("-k", help="keySpace")

    (options, args) = parser.parse_args()
    if options.b is None:
        parser.error(helper())
    server = options.b
    if options.i is None:
        parser.error(helper())
    nodeId = options.i
    if options.p is None:
        pass 
    password = options.p
    if options.a is None:
        pass 
    address = options.a
    if options.t is None:
        pass 
    tier = options.t
    if options.f is None:
        pass 
    friendly = options.f
    if options.s is None:
        pass 
    content = options.s
    if options.n is None:
        pass 
    accountNumber = options.n
    if options.k is None:
        pass 
    keySpace = options.k

    cfg = ConfigParser.RawConfigParser()
    cfg.read('key.cfg')      
    key=dict(cfg.items("Keys"))
    for x in key:
        key[x]=key[x].split("#",1)[0].strip() 
    globals().update(key)  
    accessKey = accesskey
    secretKey = secretkey

    serverStrip(server)

    serverUrl2 = "/api/appliance/" + nodeId

    urlData = {}
    try:
        password
    except NameError: 
        password = None
    if password is None:
        pass
    else:
        urlData["password"] = password
    try:
        address
    except NameError:
        address = None
    if address is None:
        pass
    else:
        urlData["ipAddress"] = address
    try:
        tier
    except NameError:
        tier = None
    if tier is None:
        pass
    else:
        urlData["serviceTier"] = tier
    try:
        friendly
    except NameError:
        friendly = None
    if friendly is None:
        pass
    else:
        urlData["userFriendlyName"] = friendly
    try:
        content
    except NameError:
        content = None
    if content is None:
        pass
    else:
        urlData["contentId"] = content
    try:
        accountNumber
    except NameError:
        accountNumber = None
    if accountNumber is None:
        pass
    else:
        urlData["accountNumber"] = accountNumber
    try:
        keySpace
    except NameError:
        keySpace = None
    if keySpace is None:
        pass
    else:
        urlData["keySpace"] = vendorKey

    headerValue = {}
    headerValue["Accept"] = 'application/json' 
    headerValue["Content-Type"] = 'application/json'

    r = Api.REST(secretKey=secretKey, accessKey=accessKey, url=serverUrl)

    serverCheck(serverName, headerValue, r, serverPort)

    prJson(r.request('PUT', serverUrl2, data=urlData, headers=headerValue))

def serverCheck(serverName, headerValue, r, serverPort):
    if platform.system() == "CYGWIN_NT-6.1":
        hiThere = "ping -n 1 " + serverName + " > /dev/null"
        if os.system(hiThere) == 0:
            socketCheck(serverName, serverPort)
            prJson(r.request('GET', '/api/appliance', headers=headerValue))
        else:
            subprocess.call('clear', shell=True)
            print "Bad IP or Address for server: "  + serverName + " is completely unreachable"
            quit()
    else:
        hiThere = "ping -c 1 " + serverName + " > /dev/null"
        if os.system(hiThere) == 0:
            socketCheck(serverName, serverPort)
            prJson(r.request('GET', '/api/appliance', headers=headerValue))
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
This script updates values for a particular node.

*   -b and -i are the only manditory switches

Usage: 
./node-update.py -b <server-ip-address> -i <node-Id> 
 -p <Password> -a <node-ip-Address> -t <service-Tier> -k <vendor-Key>
 -f <user-Friendly-name> -s <content-id> -n <accountNumber>

Example: 
./node-update.py -b 192.16.222.33 -i 14 -f "acme tnt"

 ### Please use the -h switch to list all switches for this command ### 
    '''

def prJson(data, indent=3):
    print json.dumps(data, indent=indent)


if __name__ == "__main__":
    main(sys.argv[1:])
