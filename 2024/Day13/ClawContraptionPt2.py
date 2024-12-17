import os.path
import itertools
import functools
import time
import collections
import functools
import numpy as np
import re

filename = "input.txt"
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        lines = f.read().splitlines()
    
    totalCost = 0
    prizeCount = 0
    for lineNo in range(0,len(lines),4):
        a = lines[lineNo]
        b = lines[lineNo+1]
        prize = lines[lineNo+2]
        
        ax, ay = re.findall("\\d+", a)
        bx, by = re.findall("\\d+", b)
        px, py = re.findall("\\d+", prize)
        
        left = np.array([[int(ax), int(bx)],[int(ay),int(by)]])
        right = np.array([int(px)+10000000000000, int(py)+10000000000000])
        
        aCount, bCount = np.linalg.solve(left,right)
        if round(aCount,4).is_integer() and round(bCount,4).is_integer():
            cost = aCount * 3 + bCount * 1
            prizeCount += 1
            totalCost += cost
        
    print(f"totalCost {totalCost}")
    print(f"prizeCount {prizeCount}")
        