#!/usr/bin/python

import Api
import json, sys, ConfigParser, subprocess, socket, platform, os
from optparse import OptionParser

def main(myArgs):
    parser = OptionParser()
    parser.add_option("-l", help="node admin user name")
    parser.add_option("-i", help="node ip address")
    parser.add_option("-u", help=" customer content uuid")
    parser.add_option("-p", help="node admin password")
    parser.add_option("-b", help="server ip address")
    parser.add_option("-a", help=" customer account number")
    parser.add_option("-t", help="node tier level: {10 | 30 | 50}")
    parser.add_option("-f", help="user friendly name")

    (options, args) = parser.parse_args()

    if options.f is None:
        parser.error(helper())
    friendly = options.f

    if options.l is None:
        parser.error(helper())
    userid = options.l

    if options.i is None:
        parser.error(helper())
    ip = options.i

    if options.u is None:
        parser.error(helper())
    uuid = options.u

    if options.p is None:
        parser.error(helper())
    passwd = options.p

    if options.a is None:
        parser.error(helper())
    accountnumber = options.a

    if options.t is None:
        parser.error(helper())
    tier = options.t

    if options.b is None:
        parser.error(helper())
    server = options.b

    serverStrip(server)

    #Read keys from Keys list in key.cfg
    cfg = ConfigParser.RawConfigParser()
    cfg.read('key.cfg')      
    key=dict(cfg.items("Keys"))
    for x in key:
        key[x]=key[x].split("#",1)[0].strip() 
    globals().update(key)

    theserver = server
    theAccessKey = accesskey
    theSecretKey = secretkey
    thePassWord = passwd
    theContentId = uuid
    theIpAddress = ip
    theUserName = userid
    theAccountNumber = accountnumber
    theTier = tier
    theFriendly = friendly
    
    urlData = {}
    urlData["contentId"] = theContentId
    urlData["ipAddress"] = theIpAddress
    urlData["userName"] = theUserName
    urlData["password"] = thePassWord
    urlData["keySpace"] = ""
    urlData["accountNumber"] = theAccountNumber
    urlData["serviceTier"] = theTier
    urlData["userFriendlyName"] = theFriendly

    headerValue = {}
    headerValue["Accept"] = "application/json" 
    headerValue["Content-Type"] = 'application/json'

    r = Api.REST(secretKey=theSecretKey, accessKey=theAccessKey, url=serverUrl)

    serverCheck(serverName, urlData, headerValue, r, serverPort)

def serverCheck(serverName, urlData, headerValue, r, serverPort):
    if platform.system() == "CYGWIN_NT-6.1":
        hiThere = "ping -n 1 " + serverName + " > /dev/null"
        if os.system(hiThere) == 0:
            socketCheck(serverName, serverPort)
            prJson(r.request('POST', '/api/node', data=urlData, headers=headerValue))
        else:
            subprocess.call('clear', shell=True)
            print "Bad IP or Address for server: "  + serverName + " is completely unreachable"
            quit()
    else:
        hiThere = "ping -c 1 " + serverName + " > /dev/null"
        if os.system(hiThere) == 0:
            socketCheck(serverName, serverPort)
            prJson(r.request('POST', '/api/node', data=urlData, headers=headerValue))
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
Usage: 
      ./node-add.py -u <customer-content-uuid> -i <node-ipaddr> -l admin -p <ui-admin-password> 
 -b <serverName-or-ipAddr> -a <-customer-account-number> -t <tier level { 10 | 30 | 50 }> -f <user-friendly-name>

Example: 
        ./node-add.py -u 1881 -i 10.157.199.192 -l admin -p RandomPw123 -b dorkcloud.com -a ClientTest01 -t 50 -f "ACME TNT"

        ### Please use the -h switch to list all the manditory switches for this command ### 
    '''
     
def prJson(data, indent=3):
    print json.dumps(data, indent=indent)


if __name__ == "__main__":
    main(sys.argv[1:])
