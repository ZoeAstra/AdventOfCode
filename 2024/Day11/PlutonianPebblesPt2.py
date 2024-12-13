# This one's performance really, really sucks due to getting stuck in the mental rut of my solution to part 1... 
# but I'm kind of proud that I got this technically really inefficient algorithm to actually work in a not completely unreasonable timeframe (~660s)
import os.path
import itertools
import functools
import time
import collections
import functools


def blink(stones):
    newStones = []
    tempStones = map(calculate, stones)
    for numbers in tempStones:
        newStones.extend(numbers)
    return newStones

@functools.cache
def calculate(number):
        numStr = str(number)
        if number == 0:
            return [1]
        elif len(str(number)) & 1 == 0:
            midpoint = len(numStr)//2
            return [int(numStr[:midpoint]),int(numStr[midpoint:])]
        else:
            return [number * 2024]
            

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
    
    print(stones)
    start = time.perf_counter_ns()
    lookup = { 0: [1]}
    for i in range(0,42):
        stones = blink(stones)
    
    end = time.perf_counter_ns()
    print(f"total time taken: {(end - start) / 1000000000}s")
    
    stoneCounter = collections.Counter(stones)
    stoneSet = set(stones)
    print(f"stoneset {len(stoneSet)}")
    counts = {}
    totalStones = 0
    for index, stone in enumerate(stoneSet):
        print(f"stone {index}")
        tempStones = [stone]
        start1 = time.perf_counter_ns()
        for i in range(33):
            # print(f"stone {index} blink {i}")
            tempStones = blink(tempStones)
            #tempStones = result[0]
            #lookup = result[1]
        start2 = time.perf_counter_ns()
        print(f"time taken: {(start2 - start1) / 1000000000}s")
        totalStones += len(tempStones) * stoneCounter[stone]
        
    end = time.perf_counter_ns()
    print(f"# of stones: {totalStones}")
    print(f"total time taken: {(end - start) / 1000000000}s")
    