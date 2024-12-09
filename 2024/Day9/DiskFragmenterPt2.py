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
    fileArray = []
    spaces = []
    fileIndex = 0
    for line in lines:
        pos = 0
        for index, char in enumerate(line):
            file = []
            for i in range(0,int(char)):
                if isEven(index):
                    #is file
                    array.append([fileIndex,int(char)])
                else:
                    array.append([".",int(char)])
                    #spaces.append(pos)
                pos += 1
            if isEven(index): 
                fileIndex += 1
            else: 
                spaces.append([len(array)-int(char),int(char)])
        #print("".join([str(i[0]) for i in array]))
        last = [0,0]
        for index, block in reversed(list(enumerate(array))):
            if block == last: continue
            if block[0] != "." and len(spaces) > 0:
                #file
                pop = -1
                for spaceIndex, space in enumerate(spaces):
                    if space[0] >= index: break
                    if space[1] >= block[1]:
                        for i in range(0, block[1]):
                            array[space[0]+i] = block
                            array[index-i] = [".",1]
                        space[0] += block[1]
                        space[1] -= block[1]
                        if space[1] == 0:
                            pop = spaceIndex
                        break
                if pop != -1:
                    spaces.pop(pop)
                
                # newIndex = spaces.pop(0)
                # if newIndex < index:
                #     array[newIndex] = block
                #     array[index] = "."
                # else: break
            last = block
            #print("".join([str(i[0]) for i in array]))
            #print(spaces)
        checksum = 0
        for index, block in enumerate(array):
            if block[0] != ".":
                checksum += index * block[0]
                
        print(f"checksum {checksum}")
                
        
        
        
        