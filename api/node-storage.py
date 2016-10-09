#!/usr/bin/python

import Api
import json, sys, ConfigParser, subprocess, platform, os, socket
from optparse import OptionParser

class sbcolors:
    sbGreen = '\033[92m'
    sbRed = '\033[91m'
    sbBold = '\033[1m'
    sbEnd = '\033[0m'

def main(myArgs):
    urlData = {}
    parser = OptionParser()
    parser.add_option("-i", help="node id")
    parser.add_option("-b", help="server ip address")
    parser.add_option("-p", help="storage pool: supports {dedup, snap, or perf}")
    parser.add_option("-d", help="disk: supports {sde, sdf, sdg...}")
    parser.add_option("-f", help="action: supports {add, list, or usage}")
    (options, args) = parser.parse_args()

    if options.f is None or options.i is None or options.b is None:
        subprocess.call('clear', shell=True)
        helper()
        print ""
        print sbcolors.sbRed + "Switches (-f, -b, and -i) are all manditory!" + sbcolors.sbEnd
        quit()
    elif options.f == "add" and options.d is None:
        subprocess.call('clear', shell=True)
        helper()
        print ""
        print sbcolors.sbRed + "Both switches (-d and -p) are required with (-f add)!" + sbcolors.sbEnd
        quit()
    elif options.f == "add" and options.p is None:
        subprocess.call('clear', shell=True)
        helper()
        print ""
        print sbcolors.sbRed + "Both switches (-d and -p) are required with (-f add)!" + sbcolors.sbEnd
        quit()
    elif options.f == "list" or options.f == "usage":
        if options.d != None and options.p != None:
            subprocess.call('clear', shell=True)
            helper()
            print ""
            print sbcolors.sbRed + "Either switch (-d and/or -p) are not permitted with (-f list) or (-f usage)" + sbcolors.sbEnd
            quit()
    else:
        urlData["diskName"] = options.d

    if options.p is None:
        print ""
    elif options.p == "snap":
        thePool = "act_pri_pool000"
    elif options.p == "dedup":
        thePool = "act_ded_pool000"
    elif options.p == "perf":
        thePool = "act_per_pool000"
    else:
        subprocess.call('clear', shell=True)
        print sbcolors.sbRed + "Unknown pool name. Expecting: snap, dedup, or perf" + sbcolors.sbEnd
        quit()

    thenodeId = options.i
    server = options.b
    theDisk = options.d
    theTask = options.f

    serverStrip(server)

    cfg = ConfigParser.RawConfigParser()
    cfg.read('key.cfg')      
    key=dict(cfg.items("Keys"))
    for x in key:
        key[x]=key[x].split("#",1)[0].strip() 
    globals().update(key)

    theAccessKey = accesskey
    theSecretKey = secretkey

    headerValue = {}
    headerValue["Accept"] = "application/json" 
    headerValue["Content-Type"] = 'application/json'
    
    r = Api.REST(secretKey=theSecretKey, accessKey=theAccessKey, url=serverUrl)
    serverCheck(serverName, headerValue, r, serverPort)
    if theTask == "list":
        thePost = "/api/node/" + thenodeId + "/disk"
        prJson(r.request('GET', thePost, data=urlData, headers=headerValue)) 
    elif theTask == "usage":
        thePost = "/api/node/" + thenodeId + "/usage"
        prJson(r.request('GET', thePost, data=urlData, headers=headerValue))
    elif theTask == "add":
        thePost = "/api/node/" + thenodeId + "/diskpool/" + thePool + "/disk"
        prJson(r.request('POST', thePost, data=urlData, headers=headerValue))
    else:
        subprocess.call('clear', shell=True)
        print sbcolors.sbRed + "Condition Error" + sbcolors.sbEnd
        quit()
    #print sbcolors.sbGreen + thePost + sbcolors.sbEnd

def serverCheck(serverName, headerValue, r, serverPort):
    if platform.system() == "CYGWIN_NT-6.1":
        hiThere = "ping -n 1 " + serverName + " > /dev/null"
        if os.system(hiThere) == 0:
            socketCheck(serverName, serverPort)
        else:
            subprocess.call('clear', shell=True)
            print "Bad IP or Address for server: "  + serverName + " is completely unreachable"
            quit()
    else:
        hiThere = "ping -c 1 " + serverName + " > /dev/null"
        if os.system(hiThere) == 0:
            socketCheck(serverName, serverPort)
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
    print sbcolors.sbBold + "___________________________________________________________"
    print "This script allows you to list disks attached to a node," 
    print "add disks to a pool on that node, as well as review the"
    print "usage of storage on that existing node device running."
    print "___________________________________________________________"
    print "      List disks assigned to a particular node" + sbcolors.sbEnd
    print "Usage:"
    print "./node-storage.py -f list -b <serverName-or-ipAddress> -i <node-id>"
    print ""
    print "Example:"
    print "./node-storage.py -f list -b dorkcloud.com -i 42"
    print sbcolors.sbBold + "___________________________________________________________"
    print "      List current disk usage of a particular node" + sbcolors.sbEnd
    print "Usage:"
    print "./node-storage.py -f usage -b <serverName-or-ipAddress> -i <node-id> "
    print ""
    print "Example:"
    print "./node-storage.py -f usage -b dorkcloud.com -i 42"
    print sbcolors.sbBold + "___________________________________________________________"
    print "      Add disk to a selected pool on a particular node" + sbcolors.sbEnd
    print "Usage:"
    print "./node-storage.py -f add -b <serverName-or-ipAddress> -i <node-id> \\"
    print "-p <pool-name{dedup, snap, perf}> -d <disk-for-pool>"
    print ""
    print "Example:"
    print "./node-storage.py -f add -b dorkcloud.com -i 42 -p perf -d sdg"
    print sbcolors.sbBold + "___________________________________________________________" + sbcolors.sbEnd

def prJson(data, indent=3):
    print json.dumps(data, indent=indent)

if __name__ == "__main__":
    main(sys.argv[1:])
