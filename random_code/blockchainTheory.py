#!/usr/bin/env python3

__author__ = "Stephen J. Burke"
__email__ = "steburke71@hotmail.com"
__date__ = "2/16/18"
__license__ = "GPL"

import hashlib

z = "blockchain"
s = "Stephen"
m = "Michelle"
l = "Logan"
b = "Bryson"


def bitcoin(blockchain):
    print(hashlib.sha512(str(blockchain).encode('utf-8')).hexdigest())

bitcoin(z)
bitcoin(z+s)
bitcoin(z+s+m)
bitcoin(z+s+m+l)
bitcoin(z+s+m+l+b)

