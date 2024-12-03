#Part 1 - https://adventofcode.com/2024/day/2
import os.path

filename = "input.txt"
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        lines = f.read().splitlines()

    totalSafe = 0
    for report in lines:
        trend = ""
        safe = True
        levels = report.split(" ")
        for index, level in enumerate(levels):
            if index == 0: continue
            lastLevel = levels[index-1]
            diff = int(level) - int(lastLevel)
            if abs(diff) < 1 or abs(diff) > 3: 
                safe = False
                break
            if index == 1:
                trend = "increasing" if diff > 0 else "decreasing"
            if diff < 0 and trend == "increasing":
                safe = False
                break
            if diff > 0 and trend == "decreasing":
                safe = False
                break
        if safe: totalSafe += 1

    print(f"the total number of safe reports is: {totalSafe}")