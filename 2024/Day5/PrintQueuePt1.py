import os.path
from functools import reduce

filename = "input.txt"
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        lines = f.read().splitlines()
    
    reachedSecondSet = False
    rules = dict()
    #values are what pages must be before the key page (if they occur)
    updates = []
    for line in lines:
        if line == "":
            reachedSecondSet = True
            continue
        if reachedSecondSet:
            update = []
            for page in line.split(","):
                update.append(int(page))
            updates.append(update)
        else:
            rule = line.split("|")
            after = int(rule[1])
            before = int(rule[0])
            if after in rules:
                rules[after].add(before)
            else:
                rules[after] = set([before])
        
    middles = []
    for update in updates:
        disallowed = set([])
        correct = True
        for page in update:
            rule = set([])
            if page in rules:
                rule = rules[page]
            disallowed = disallowed.union(rule)
            if page in disallowed:
                correct = False
                break
        if correct:
            middles.append(update[int(len(update)/2)])
            
    
    total = reduce(lambda x, y: x + y, middles, 0)
    print(f"total: {total}")