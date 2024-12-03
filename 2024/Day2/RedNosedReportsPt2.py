#Part 2 - https://adventofcode.com/2024/day/2#part2
import os.path

def originalAndMinusOnePermutations(list):
    yield list
    for index, item in enumerate(list):
        copy = list.copy()
        copy.pop(index)
        yield copy

# Testing
# for perm in originalAndMinusOnePermutations([1,2,3,4,5,6,7,8,9,0]):
#   print(perm)

filename = "input.txt"
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        lines = f.read().splitlines()

    totalSafe = 0
    for report in lines:
        originalLevels = report.split(" ")
        anySafe = False
        for levels in originalAndMinusOnePermutations(originalLevels):
            trend = ""
            safe = True
            for index, level in enumerate(levels):
                if index == 0: continue
                lastLevel = levels[index-1]
                diff = int(level) - int(lastLevel)
                if abs(diff) < 1 or abs(diff) > 3: 
                    safe = False
                    break
                if trend == "":
                    trend = "increasing" if diff > 0 else "decreasing"
                if diff < 0 and trend == "increasing":
                    safe = False
                    break
                if diff > 0 and trend == "decreasing":
                    safe = False
                    break
            if safe: 
                totalSafe += 1
                anySafe = True
                break

    print(f"the total number of safe reports is: {totalSafe}")