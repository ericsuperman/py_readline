#!/usr/bin/python3

import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
if len(sys.argv) != 2:
	print ("Usage:\n") 
	sys.exit()

with open(sys.argv[1]) as f:
    for line in f:
        print(line) 

f.close()

