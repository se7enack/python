#!/usr/bin/env python3

__author__ = "Stephen J. Burke"
__email__ = "steburke71@hotmail.com"
__date__ = "2/19/18"
__license__ = "GPL"

nighthawksTup = "Nighthawks at the Diner", "Tom Waits", 1975, "Rock", ((1, "Emotional Weather Report"), (2, "On a Foggy Night"), (3, "Eggs and Sausage (In a Cadillac with Susan Michelson)"), (4, "Better Off Without a Wife"), (5, "Nighthawk Postcards (From Easy Street)"), (6, "Warm Beer and Cold Women"), (7, "Putnam County"), (8, "Spare Parts I (A Nocturnal Emission)"), (9, "Nobody"), (10, "Big Joe and Phantom 309"), (11, "Spare Parts II and Closing"),)
title, artist, year, genre, tracks = nighthawksTup
print(title)
print(artist)
print(year)
print(genre)
print('Tracks:')
for song in tracks:
    track, title = song
    print('\t' + str(title))


