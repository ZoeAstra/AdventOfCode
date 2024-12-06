import os.path
import copy

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
            
def move(pos,direction):
    return [pos[0]+direction[0],pos[1]+direction[1]]

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
    obstructions = []
    for num, line in enumerate(lines):
        row = []
        for index, char in enumerate(line):
            row.append(char)
            if char == "^":
                currentPosition = [num, index]
            if char == "#":
                obstructions.append([num, index])
        array.append(row)
        
    oPos = copy.deepcopy(currentPosition)
    oDir = copy.deepcopy(currentDirection)
    oArray = copy.deepcopy(array)
    
    while True:
        #print(f"currentPosition {currentPosition}")
        array[currentPosition[0]][currentPosition[1]] = "X"
        nextPos = move(currentPosition,currentDirection)
        #print(f"nextPos {nextPos}")
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
        array[y][x] = "#"
        while True:
            if [currentPosition,currentDirection] in posDirLog:
                loopCount += 1
                break
            posDirLog.append([currentPosition,currentDirection])
            array[currentPosition[0]][currentPosition[1]] = "X"
            nextPos = move(currentPosition,currentDirection)
            if nextPos[0] == ymax or nextPos[0] < 0 or nextPos[1] == xmax or nextPos[1] < 0:
                break
            if array[nextPos[0]][nextPos[1]] == "#":
                currentDirection = nextDirection(currentDirection)
                continue
            currentPosition = nextPos
    
    print(f"total {loopCount}")
            