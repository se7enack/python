#!/usr/bin/env python3

__author__ = "Stephen J. Burke"
__email__ = "steburke71@hotmail.com"
__date__ = "2/14/18"
__license__ = "GPL"

beers = []
beers.append(['sam adams', 'harpoon ipa', 'bass ale'])
beers.append(['hefenrefer', 'corona light', 'bud light'])
beers.append(['heineken', 'blue moon', 'bud light'])

# print(beer)

# take me to a place with decent beer
for beer in beers:
    if not 'bud light' in beer:
        for i in beer:
            print(i)
