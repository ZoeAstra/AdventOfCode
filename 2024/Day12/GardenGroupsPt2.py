import os.path
import itertools
import functools
import time
import collections
import functools

def vector_add(a, b):
    return (a[0]+b[0],a[1]+b[1])
    
def outOfBounds(x, y, xmax, ymax):
    x = int(x)
    y = int(y)
    return y >= ymax or y < 0 or x >= xmax or x < 0

def reverseDirection(currentDirection):
    match currentDirection:
        case [0,1]:
            return [-1,0]
        case [1,0]:
            return [0,1]
        case [0,-1]:
            return [1,0]
        case [-1,0]:
            return [0,-1]
            
def nextDirection(currentDirection):
    match currentDirection:
        case [-1,0]:
            return [0,1]
        case [0,1]:
            return [1,0]
        case [1,0]:
            return [0,-1]
        case [0,-1]:
            return [-1,0]

def getPlant(pos, garden):
    if outOfBounds(pos[1], pos[0], len(garden[0]), len(garden)):
        return ""
    return garden[pos[0]][pos[1]]
    
def veggiePlot(pos, garden, visited):
    north = [-1,0]
    east = [0,1]
    south = [1,0]
    west = [0,-1]
    directions = [north,east,south,west]
    totalArea = 0
    totalSides = 0
    y = pos[0]
    x = pos[1]
    visited.add((y,x))
    veggie = garden[y][x]
    
    # check north
    if getPlant(vector_add(pos,north),garden) != veggie and (getPlant(vector_add(pos,west),garden) != veggie or getPlant(vector_add(vector_add(pos,west),north),garden) == veggie):
        totalSides +=1
    # east
    if getPlant(vector_add(pos,east),garden) != veggie and (getPlant(vector_add(pos,north),garden) != veggie or getPlant(vector_add(vector_add(pos,east),north),garden) == veggie):
        totalSides +=1
    # south
    if getPlant(vector_add(pos,south),garden) != veggie and (getPlant(vector_add(pos,east),garden) != veggie or getPlant(vector_add(vector_add(pos,east),south),garden) == veggie):
        totalSides +=1
    # weast
    if getPlant(vector_add(pos,west),garden) != veggie and (getPlant(vector_add(pos,south),garden) != veggie or getPlant(vector_add(vector_add(pos,west),south),garden) == veggie):
        totalSides +=1
    
    for direction in directions:
        nextY, nextX = vector_add(pos, direction)
        if outOfBounds(nextX, nextY, len(garden[0]), len(garden)):
            continue
        if garden[nextY][nextX] == veggie:
            if (nextY, nextX) in visited: continue
            newArea, newSides, newVisited = veggiePlot([nextY, nextX], garden, visited)
            totalArea += newArea
            totalSides += newSides
            visited |= newVisited
            continue
    return (totalArea+1, totalSides, visited)

filename = "input.txt"
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        lines = f.read().splitlines()
    
    garden = []
    for line in lines:
        veggies = []
        for char in line:
            veggies.append(char)
        garden.append(veggies)
    
    xmax = len(garden)
    ymax = len(garden[0])
    
    visited = set()
    
    currentVeggie = ""
    totalSides = 0
    totalArea = 0
    regions = []
    for y, row in enumerate(garden):
        for x, veggie in enumerate(row):
            if (y,x) not in visited:
                newArea, newSides, newVisited = veggiePlot([y, x], garden, visited)
                regions.append([(y,x), veggie, newArea, newSides])
                totalArea += newArea
                totalSides += newSides
                visited = newVisited
    
    totalPrice = functools.reduce(lambda x, y: x + (y[2] * y[3]), regions, 0)
        
    print(f"totalPrice: {totalPrice}")