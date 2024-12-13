# This second solution to pt2 is much more efficient and probably the intended way... 
# Took me a bit and some (not insubstantial) hints from a friend, but I got this to work to a point I'm happy with (~.25s)
# I'm almost tempted to just record this v2, but I think this and v1 serves as a reminder that sometimes you need to start over from the beginning to get fresh perspective and a better solution
import os.path
import itertools
import functools
import time
import collections
import functools

@functools.cache
def count(number, generation, maximum):
    if generation == maximum: return 1
    numStr = str(number)
    if len(numStr) & 1 == 0:
        midpoint = len(numStr)//2
        return count(int(numStr[:midpoint]), generation + 1, maximum) + count(int(numStr[midpoint:]), generation + 1, maximum)
    return count(1 if number == 0 else number * 2024, generation + 1, maximum)
            

filename = "input.txt"
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        lines = f.read().splitlines()
    
    stones = []
    line = lines[0]
    for number in line.split(" "):
        stones.append(int(number))
    
    maximum = 75
    start = time.perf_counter_ns()
    totalStones = functools.reduce(lambda x, y: x + count(y, 0, maximum), stones, 0)
    
    end = time.perf_counter_ns()
    print(f"# of stones: {totalStones}")
    print(f"total time taken: {(end - start) / 1000000000}s")
