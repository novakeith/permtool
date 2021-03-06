#!/usr/bin/env python3
#permutation tool - generate permutations then do operations based on those permutations
#the operations are in the successive "if" section on lines 19-26
#this code is to help solve a cybersec challenge; might be useful for something else in the future

from itertools import permutations
from decimal import *
getcontext().prec = 16
import sys
f = open("output.txt", "w")

#need a number to operate on, exit otherwise
if len(sys.argv) != 2:
    sys.exit("Incorrect syntax, try: ./permtool.py <number>")

num = Decimal(sys.argv[1]) #get the number
perm = permutations(["A","B","C","D"])
out = num
ctr = 1

for x in perm:
    for i in x:
        if i == "A":
            out = out + Decimal(5)
        if i == "B":
            out = out - Decimal(3.14)
        if i == "C":
            out = out * Decimal(120)
        if i == "D":
            out = out / Decimal(3)
    print ("Permutation " + str(ctr) + ": " + str(out) + "\n")
    f.write(str(ctr) + ": " + str(out) + "\n")
    out = num
    ctr += 1
print("Complete")
f.close()
