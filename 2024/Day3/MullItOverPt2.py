import os.path
import re

filename = "input.txt"
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        lines = f.read().splitlines()
          
    total = 0
    instructions = ""
    for instruction in lines:
        instructions += instruction

    for doBlock in re.split(r"do\(\)",instructions):
        doInstruction = re.split(r"don\'t\(\)",doBlock)[0]
        for mul in re.findall(r"mul\(\d+,\d+\)",doInstruction):
            nums = mul[4:-1].split(",")
            total += int(nums[0])*int(nums[1])
                                                    
print(f"total: {total}")