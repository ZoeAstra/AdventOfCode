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
    
def veggiePlot(position, garden, visited):
    directions = [[-1,0],[0,1],[1,0],[0,-1]]
    totalArea = 0
    totalPerimeter = 0
    y = position[0]
    x = position[1]
    visited.add((y,x))
    veggie = garden[y][x]
    for direction in directions:
        nextY, nextX = vector_add(position, direction)
        if outOfBounds(nextX, nextY, len(garden[0]), len(garden)):
            totalPerimeter += 1
            continue
        
        if garden[nextY][nextX] == veggie:
            if (nextY, nextX) in visited: continue
            newArea, newPerimeter, newVisited = veggiePlot([nextY, nextX], garden, visited)
            totalArea += newArea
            totalPerimeter += newPerimeter
            visited |= newVisited
            continue
        totalPerimeter += 1
            
    return (totalArea+1, totalPerimeter, visited)

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
    totalPerimeter = 0
    totalArea = 0
    regions = []
    for y, row in enumerate(garden):
        for x, veggie in enumerate(row):
            if (y,x) not in visited:
                newArea, newPerimeter, newVisited = veggiePlot([y, x], garden, visited)
                regions.append([[y,x], veggie, newArea, newPerimeter])
                totalArea += newArea
                totalPerimeter += newPerimeter
                visited = newVisited
    
    totalPrice = functools.reduce(lambda x, y: x + (y[2] * y[3]), regions, 0)
    print(f"totalPrice: {totalPrice}")
    