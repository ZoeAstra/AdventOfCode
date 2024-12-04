import os.path
import re

filename = "input.txt"
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
            lines = f.read().splitlines()
                    
                        
    array = []
    aLocations = []
    for row, line in enumerate(lines):
        array.append(list(line))
        for column, letter in enumerate(line):
            if letter == "A": aLocations.append([row, column])
                                                                        
    ymax = len(array)
    xmax = len(array[0])
    #print(f"xmax: {xmax}")
    #print(f"ymax: {ymax}")
    count = 0
    for location in aLocations:
        row = location[0]
        column = location[1]
        #print(location)
        masCount = 0
        for x in [1,-1]:
            for y in [1,-1]:
                # all possible corner directional permutations
                #print(f"{y}{x}")
                my = row+y
                mx = column+x
                if my >= 0 and my < ymax and mx >= 0 and mx < xmax and array[my][mx] == "M":
                    #print(f"found m at {my},{mx}") 
                    sy = row+(0-y)
                    sx = column+(0-x)
                    if sy >= 0 and sy < ymax and sx >= 0 and sx < xmax and array[sy][sx] == "S":
                        #print(f"found s at {sy},{sx}. count +1") 
                        masCount += 1
                        if masCount == 2: count += 1
    print(f"total X-MASes: {count}")