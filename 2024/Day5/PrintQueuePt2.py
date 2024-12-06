import os.path
import functools

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
        if not correct:
            def test(a,b): 
                rule = set([])
                if b in rules:
                    rule = rules[a]
                if a in rule: return -1
                if a in rules:
                    rule = rules[a]
                if b in rule: return 1
                return 0
            corrected = sorted(update, key=functools.cmp_to_key(test))
            # take two values
            # output -1 if left needs to go before right
            # 0 if it doesnt matter
            # +1 if right goes before left
            middles.append(corrected[int(len(corrected)/2)])
            
    
    total = functools.reduce(lambda x, y: x + y, middles, 0)
    print(f"total: {total}")