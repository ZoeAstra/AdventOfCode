import os.path
import copy
import time

startTime = time.perf_counter_ns()

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
            
def move(pos, direction):
    return [pos[0]+direction[0],pos[1]+direction[1]]

#useful for debugging what the heck this was doing
def printArray(array):
    for row in array:
        str = ""
        for col in row:
            str += col
        print(str)

def nextObstruction(pos, direction, obstructions):
    result = []
    match direction:
        case [-1,0]:
            result = sorted([i for i in list(obstructions) if i[0] < pos[0] and i[1] == pos[1]], key = lambda x: x[0], reverse=True)
        case [0,1]:
            result = sorted([i for i in list(obstructions) if i[1] > pos[1] and i[0] == pos[0]], key = lambda x: x[1])
        case [1,0]:
            result = sorted([i for i in list(obstructions) if i[0] > pos[0] and i[1] == pos[1]], key = lambda x: x[0])
        case [0,-1]:
            result = sorted([i for i in list(obstructions) if i[1] < pos[1] and i[0] == pos[0]], key = lambda x: x[1], reverse=True)
    return [] if len(result) == 0 else result[0]

filename = "input.txt"
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        lines = f.read().splitlines()
    ymax = len(lines)
    xmax = len(lines[0])
    array = []
    currentPosition = [0,0]
    currentDirection = [-1,0]
    obstructions = set()
    for num, line in enumerate(lines):
        row = []
        for index, char in enumerate(line):
            row.append(char)
            if char == "^":
                currentPosition = [num, index]
            if char == "#":
                obstructions.add((num, index))
        array.append(row)
        
    oPos = copy.deepcopy(currentPosition)
    oDir = copy.deepcopy(currentDirection)
    oArray = copy.deepcopy(array)
    oObstructions = copy.deepcopy(obstructions)
    
    while True:
        array[currentPosition[0]][currentPosition[1]] = "X"
        nextPos = move(currentPosition,currentDirection)
        if nextPos[0] == ymax or nextPos[0] < 0 or nextPos[1] == xmax or nextPos[1] < 0:
            break
        if array[nextPos[0]][nextPos[1]] == "#":
            currentDirection = nextDirection(currentDirection)
            continue
        currentPosition = nextPos
        
    candidates = []
    for y, row in enumerate(array):
        for x, col in enumerate(row):
            if col == "X": candidates.append([y,x])
    
    print(f"candidates# {len(candidates)}")
    loopCount = 0
    for num, candidate in enumerate(candidates):
        print(f"candidate {num}")
        y = candidate[0]
        x = candidate[1]
        if [y,x] == oPos or oArray[y][x] == "#":
            continue
        posDirLog = []
        currentPosition = copy.deepcopy(oPos)
        currentDirection = copy.deepcopy(oDir)
        array = copy.deepcopy(oArray)
        obstructions = copy.deepcopy(oObstructions)
        obstructions.add((y,x))
        array[y][x] = "#"
        while True:
            if [currentPosition,currentDirection] in posDirLog:
                loopCount += 1
                break
            array[currentPosition[0]][currentPosition[1]] = "X"
            posDirLog.append([currentPosition,currentDirection])
            nextObs = nextObstruction(currentPosition,currentDirection, obstructions)
            if nextObs == []:
                # only empty if no obstacle ahead, which means FREEDOM!
                break
            nextPos = move(nextObs, nextDirection(nextDirection(currentDirection))) #do a 360 and moonwalk "forward" one space off of the obstruction
            currentDirection = nextDirection(currentDirection)
            currentPosition = nextPos
    
    endTime = time.perf_counter_ns()
    print(f"total {loopCount} in {(endTime - startTime)/1000000000}s")
            