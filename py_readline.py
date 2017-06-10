#!/usr/bin/python3

import sys

def oneline(line):
    print(line)

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
if len(sys.argv) != 2:
	print ("Usage:\n") 
	sys.exit()

with open(sys.argv[1]) as f:
    for line in f:
        oneline(line) 

f.close()

