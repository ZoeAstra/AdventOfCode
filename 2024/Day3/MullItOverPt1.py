import os.path
import re

filename = "input.txt"
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        lines = f.read().splitlines()
            
    total = 0
    for instruction in lines:
        for mul in re.findall(r"mul\(\d+,\d+\)",instruction):
            nums = mul[4:-1].split(",")
            total += int(nums[0])*int(nums[1])
                 
print(f"total: {total}")