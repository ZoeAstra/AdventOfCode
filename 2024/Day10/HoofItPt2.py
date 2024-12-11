import os.path
import itertools
import functools

def vector_add(a, b):
    return [a[0]+b[0],a[1]+b[1]]
    
def outOfBounds(x, y, xmax, ymax):
    x = int(x)
    y = int(y)
    return y >= ymax or y < 0 or x >= xmax or x < 0

def score(array, location):
    y = location[0]
    x = location[1]
    currentValue = array[y][x]
    total = 0
    limit = 9
    directions = [[-1,0],[0,1],[1,0],[0,-1]]
    for direction in directions:
        nextLocation = vector_add(location, direction)
        if outOfBounds(nextLocation[1],nextLocation[0],len(array),len(array)):
            continue
        nextValue = array[nextLocation[0]][nextLocation[1]]
        if nextValue == currentValue + 1:
            if nextValue == limit:
                total += 1
                continue
            total += score(array, nextLocation)
    return total

filename = "input.txt"
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        lines = f.read().splitlines()
    
    array = []
    trailheads = []
    for row, line in enumerate(lines):
        positions = []
        for col, pos in enumerate(line):
            positions.append(int(pos))
            if int(pos) == 0:
                trailheads.append([row,col])
        array.append(positions)
    
    totalScore = 0
    for trailhead in trailheads:
        totalScore += score(array,trailhead)
        
    print(f"total score: {totalScore}")
            