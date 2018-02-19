#!/usr/bin/env python3

__author__ = "Stephen J. Burke"
__email__ = "steburke71@hotmail.com"
__date__ = "2/19/18"
__license__ = "GPL"

#Tuple
# nighthawksTup = "Nighthawks at the Diner", "Tom Waits", 1979
# title, artist, year = nighthawksTup
# print(artist)

# nighthawksTup = "Nighthawks at the Diner", "Tom Waits", 1979, "Rock", (1, "Emotional Weather Report"), (2, "Better off without a wife")
# title, artist, year, genre, track1, track2 = nighthawksTup
# print(track2)

nighthawksTup = "Nighthawks at the Diner", "Tom Waits", 1975, "Rock", ((1, "Emotional Weather Report"), (2, "On a Foggy Night"), (3, "Eggs and Sausage (In a Cadillac with Susan Michelson)"), (4, "Better Off Without a Wife"), (5, "Nighthawk Postcards (From Easy Street)"), (6, "Warm Beer and Cold Women"), (7, "Putnam County"), (8, "Spare Parts I (A Nocturnal Emission)"), (9, "Nobody"), (10, "Big Joe and Phantom 309"), (11, "Spare Parts II and Closing"),)
title, artist, year, genre, tracks = nighthawksTup
x = range(0, len(tracks))
for track in x:
    print(tracks[track], end='\t')


