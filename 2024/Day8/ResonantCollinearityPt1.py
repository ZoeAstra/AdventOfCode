
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
    
    printArray(array)
    print()
    antiCount = 0
    ymax = len(array)
    xmax = len(array[0])
    for antenna, locations in antennae.items():
        print(f"ant {antenna}")
        print(f"loc {locations}")
        for perm in list(itertools.combinations(locations, 2)):
            print(f"perm {perm}")
            one = perm[0]
            two = perm[1]
            diff1 = [one[0]-two[0],one[1]-two[1]]
            diff2 = [two[0]-one[0],two[1]-one[1]]
            candidate1 = [one[0]-diff2[0],one[1]-diff2[1]]
            candidate2 = [two[0]-diff1[0],two[1]-diff1[1]]
            print(f"candidate1 {candidate1}")
            print(f"candidate2 {candidate2}")
            if not outOfBounds(candidate1[0],candidate1[1],xmax,ymax):
                print("can1")
                if array[candidate1[0]][candidate1[1]] != "#":
                    antiCount += 1
                    array[candidate1[0]][candidate1[1]] = "#"
            if not outOfBounds(candidate2[0],candidate2[1],xmax,ymax):
                print("can2")
                if array[candidate2[0]][candidate2[1]] != "#":
                    antiCount += 1
                    array[candidate2[0]][candidate2[1]] = "#"
    printArray(array)
    print(f"total antinodes: {antiCount}")