#Part 1 - https://adventofcode.com/2024/day/1
import os.path

filename = "input.txt"
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        lines = f.read().splitlines()
          
    # I tried to be clever here at first and sort everything together as one big list, 
    # but then i did the math and at an O(n log(n)) worst case timescale (as the python 
    # powersort algorithm is), sorting a list of size 2n is slower than sorting two 
    # lists of size n... specifically about ~10% slower with n = 1000. yay, math!
    numbers1 = []
    numbers2 = []
    for line in lines:
        numbers = line.split("   ")
        numbers1.append(int(numbers[0]))
        numbers2.append(int(numbers[1]))
                                
    numbers1.sort()
    numbers2.sort()
    totalDistance = 0
                                        
    for index, number in enumerate(numbers1):
        totalDistance += abs(number - numbers2[index])
                                                
    print(f"the total distance of the provided lists is: {totalDistance}")