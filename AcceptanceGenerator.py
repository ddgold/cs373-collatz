#!/usr/bin/env python

"""
Program used to generate acceptence test
"""

from random import randrange, seed

for i in range(0,1000) :
	if i % 10 == 0:
		seed(i / 10)
	b = randrange(1, 100000)
	e = randrange(1, 100000)
	print str(b) + " " + str(e)