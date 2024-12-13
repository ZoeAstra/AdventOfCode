import os.path
import itertools
import functools

def blink(array):
    newArray = []
    for number in array:
        numStr = str(number)
        if number == 0:
            newArray.append(1)
        elif len(str(number)) % 2 == 0:
            #print(numStr)
            #print(int(len(numStr)/2))
            newArray.append(int(numStr[:int(len(numStr)/2)]))
            newArray.append(int(numStr[int(len(numStr)/2):]))
        else:
            newArray.append(number * 2024)
    return newArray
            

filename = "input.txt"
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        lines = f.read().splitlines()
    
    array = []
    line = lines[0]
    for number in line.split(" "):
        array.append(int(number))
    
    for i in range(0,25):
        print(f"blink {i}")
        array = blink(array)
        
    #print(array)
    print(f"# of stones: {len(array)}")
    