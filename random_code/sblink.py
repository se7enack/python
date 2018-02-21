#!/usr/bin/env python3

__author__ = "Stephen J. Burke"
__email__ = "steburke71@hotmail.com"
__date__ = "2/20/18"
__license__ = "GPL"

import requests

baseUrl = 'rest.prod.immedia-semi.com'


def banner():
    print("""
   .--.--.       ,---,.   ,--,                              ,-.  
  /  /    `.   ,`  .`  \,--.`|     ,--,                 ,--/ /|  
 |  :  /`. / ,---.` .` ||  | :   ,--.`|         ,---, ,--. :/ |  
 ;  |  |--`  |   |  |: |:  : `   |  |,      ,-+-. /  |:  : ` /   
 |  :  ;_    :   :  :  /|  ` |   `--`_     ,--.`|`   ||  `  /    
  \  \    `. :   |    ; `  | |   ,` ,`|   |   |  ,`` |`  |  :    
   `----.   \|   :     \|  | :   `  | |   |   | /  | ||  |   \   
   __ \  \  ||   |   . |`  : |__ |  | :   |   | |  | |`  : |. \  
  /  /`--`  /`   :  `; ||  | `.`|`  : |__ |   | |  |/ |  | ` \ \ 
 `--`.     / |   |  | ; ;  :    ;|  | `.`||   | |--`  `  : |--`  
   `--`---`  |   :   /  |  ,   / ;  :    ;|   |/      ;  |,`     
             |   | ,`    ---`-`  |  ,   / `---`       `--`       
             `----`               ---`-`                         
          """)


banner()

choices = ((1, "Download all videos", "SB_TO_COME_BACK_TO"), (2, "Get network information", "/networks"),
           (3, "Get Sync Module information", "/network/${NETWORKID}/syncmodules"),
           (4, "Arm network", "/network/${NETWORKID}/arm"), (5, "Disarm network", "/network/${NETWORKID}/disarm"),
           (6, "Get homescreen information", "/homescreen"),
           (7, "Get events for network", "/events/network/${NETWORKID}"),
           (8, "Capture a new thumbnail", "/network/${NETWORKID}/camera/${CAMERAID}/thumbnail"),
           (9, "Capture a new video", "/network/${NETWORKID}/camera/${CAMERAID}/clip"),
           (10, "Get a total on the number of videos", "/api/v2/videos/count"),
           (11, "Get paginated video information", "SB_TO_COME_BACK_TO"),
           (12, "Unwatched video list", "/api/v2/videos/unwatched"),
           (13, "Get a list of all cameras", "/network/${NETWORKID}/cameras"),
           (14, "Get camera information", "/network/${NETWORKID}/camera/${CAMERAID}"),
           (15, "Get camera sensor information", "/network/${NETWORKID}/camera/${CAMERAID}/signals"),
           (16, "Enable motion detection", "/network/${NETWORKID}/camera/${CAMERAID}/enable"),
           (17, "Disable motion detection", "/network/${NETWORKID}/camera/${CAMERAID}/disable"),
           (18, "Get information about connected devices", "/account/clients"),
           (19, "Get information about supported regions", "/regions"),
           (20, "Get information about system health", "/health"),
           (21, "Get information about programs", "/api/v1/networks/${NETWORKID}/programs")), 'exit'
options, bye = choices
maxSize = len(options)

for option in options:
    num, msg, call = option
    print(str(num) + '\t' + msg)

pick = int(input('\nChoose a number between 1 and {0}: '.format(maxSize)))
if pick in range(1, maxSize + 1):
    for option in options:
        num, msg, call = option
        if num == pick:
            fullUrl = 'https://' + baseUrl + call
            r = requests.get(fullUrl)
            print(r.content)
else:
    print('expected a number between 1-{0}, however got {1}...'.format(maxSize, pick))
    print('please try again')
