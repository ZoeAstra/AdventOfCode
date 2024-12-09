import os.path
import itertools
import functools

def isEven(num):
    if num % 2:
        return False
    else:
        return True

filename = "input.txt"
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        lines = f.read().splitlines()
    
    array = []
    spaces = []
    fileIndex = 0
    for line in lines:
        pos = 0
        for index, char in enumerate(line):
            for i in range(0,int(char)):
                if isEven(index):
                    #is file
                    array.append(fileIndex)
                else:
                    array.append(".")
                    spaces.append(pos)
                pos += 1
            if isEven(index): fileIndex += 1
        #print("".join([str(i) for i in array]))
        for index, block in reversed(list(enumerate(array))):
            if block != "." and len(spaces) > 0:
                #file
                newIndex = spaces.pop(0)
                if newIndex < index:
                    array[newIndex] = block
                    array[index] = "."
                else: break
            #print("".join([str(i) for i in array]))
            #print(spaces)
        checksum = 0
        for index, block in enumerate(array):
            if block != ".":
                checksum += index * block
                
        print(f"checksum {checksum}")
                
        
        
        
        