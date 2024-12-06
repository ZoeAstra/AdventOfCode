import os.path
import functools

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
    
    while True:
        array[currentPosition[0]][currentPosition[1]] = "X"
        nextPos = move(currentPosition,currentDirection)
        if nextPos[0] == ymax or nextPos[0] < 0 or nextPos[1] == xmax or nextPos[1] < 0:
            break
        if array[nextPos[0]][nextPos[1]] == "#":
            currentDirection = nextDirection(currentDirection)
            continue
        currentPosition = nextPos
    
    total = 0
    for row in array:
        for col in row:
            if col == "X": total += 1
    
    print(f"total {total}")
            