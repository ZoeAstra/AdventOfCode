
import os.path
import itertools
import functools

    
def printArray(array):
    for row in array:
        s = ""
        for col in row:
            s += str(col)
        print(s)
        
def outOfBounds(x, y, xmax, ymax):
    x = int(x)
    y = int(y)
    return y >= ymax or y < 0 or x >= xmax or x < 0

filename = "input.txt"
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        lines = f.read().splitlines()
    
    antennae = dict()
    array = []
    for row, line in enumerate(lines):
        array.append([])
        for col, char in enumerate(line):
            array[row].append(char)
            if char == ".":
                continue
            if char not in antennae: 
                antennae[char] = [[row,col]]
            else: 
                antennae[char].append([row,col])
    
    #printArray(array)
    antiCount = 0
    ymax = len(array)
    xmax = len(array[0])
    for antenna, locations in antennae.items():
        #print(f"ant {antenna}")
        #print(f"loc {locations}")
        for perm in list(itertools.combinations(locations, 2)):
            #print(f"perm {perm}")
            one = perm[0]
            two = perm[1]
            diff1 = [one[0]-two[0],one[1]-two[1]]
            diff2 = [two[0]-one[0],two[1]-one[1]]
            nextPos = one
            while not outOfBounds(nextPos[0],nextPos[1], xmax, ymax):
                if array[nextPos[0]][nextPos[1]] != "#":
                    antiCount += 1
                    array[nextPos[0]][nextPos[1]] = "#"
                nextPos = [nextPos[0]-diff2[0],nextPos[1]-diff2[1]]
            nextPos = two
            while not outOfBounds(nextPos[0],nextPos[1],xmax,ymax):
                if array[nextPos[0]][nextPos[1]] != "#":
                    antiCount += 1
                    array[nextPos[0]][nextPos[1]] = "#"
                nextPos = [nextPos[0]-diff1[0],nextPos[1]-diff1[1]]
    #printArray(array)
    print(f"total antinodes: {antiCount}")