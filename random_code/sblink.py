#!/usr/bin/env python3

__author__ = "Stephen J. Burke"
__email__ = "steburke71@hotmail.com"
__date__ = "2/20/18"
__license__ = "GPL"

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

choices = {
    1: "Download all videos",
    2: "Get network information",
    3: "Get Sync Module information",
    4: "Arm network",
    5: "Disarm network",
    6: "Get homescreen information",
    7: "Get events for network",
    8: "Capture a new thumbnail",
    9: "Capture a new video",
    10: "Get a total on the number of videos",
    11: "Get paginated video information",
    12: "Unwatched video list",
    13: "Get a list of all cameras",
    14: "Get camera information",
    15: "Get camera sensor information",
    16: "Enable motion detection",
    17: "Disable motion detection",
    18: "Get information about connected devices",
    19: "Get information about supported regions",
    20: "Get information about system health",
    21: "Get information about programs",
    22: "Quit"
}

inOrder = sorted(list(choices.keys()))
maxSize = len(inOrder)
for number in inOrder:
    print(str(number) + ' - ' + str(choices[number]))

while True:
    try:
        option = int(input('\nChoose a number between 1 and {0}: '.format(maxSize)))
        if option == maxSize:
            print('you chose to quit, now exiting!')
            break
        if option in inOrder:
            print('is a number between 1-{0}'.format(maxSize))
        else:
            print('expected a number between 1-{0}, however got {1}...'.format(maxSize, option))
            print('please try again')
    except:
        print("Error: Value entered was not a valid integer, now exiting.")
        break

# r = requests.get('https://' + baseUrl)
# print(r.content)
