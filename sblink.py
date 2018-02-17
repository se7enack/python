#!/usr/bin/env python3

import os
import getpass

blinkUrl = "rest.prod.immedia-semi.com"
sblinkDir = "/tmp/sblink"
urlFile = sblinkDir + "/" + "url"
authFile = sblinkDir + "/" + "auth"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def challenge():
  try:
      u = getpass._raw_input("\n\nEnter username: ")
      p = getpass.getpass()
  except Exception as err:
      print('ERROR:', err)
  else:
      print('You entered:', u, p)


def splash():
  print(''' \n
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
  ''')

def createUrlFile(sblinkDir,urlFile):
  basedir = os.path.dirname(sblinkDir)
  if not os.path.exists(basedir):
      os.makedirs(sblinkDir)
      def touch(urlFile):
        with open(urlFile, 'a'):
            os.utime(urlFile, None)
      f = open(urlFile, "w")
      f.write("\nsb")
      f.close()

def createAuthFile(authFile):
  with open(authFile, 'r') as data:
    auth = data.read().replace('\n', '')
    print(auth)

clear()
splash()
challenge()
createUrlFile(sblinkDir,urlFile)
createAuthFile(authFile)




