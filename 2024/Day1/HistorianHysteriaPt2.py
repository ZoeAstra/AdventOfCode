# Part2 - https://adventofcode.com/2024/day/1
import os.path
from collections import Counter

filename = "input.txt"
if not os.path.isfile(filename):
  print('File does not exist.')
else:
    with open(filename) as f:
        lines = f.read().splitlines()
          
    numbersLeft = []
    numbersRight = []
    for line in lines:
        numbers = line.split("   ")
        numbersLeft.append(int(numbers[0]))
        numbersRight.append(int(numbers[1]))
                            
    counterRight = Counter(numbersRight)
    counterLeft = Counter(numbersLeft)
                                
    totalSimilarity = 0
    for key, value in counterLeft.items():
        totalSimilarity += key * value * counterRight[key]
                                            
    print(f"the total similarity score of the left list to the right list is: {totalSimilarity}")