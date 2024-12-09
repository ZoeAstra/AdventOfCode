import os.path
import itertools
import functools

filename = "input.txt"
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        lines = f.read().splitlines()
        
    ops = ["*","+","||"]
    def operate(a,b,op):
        match op:
            case "+":
                return a + b
            case "*":
                return a * b
            case "||":
                return int(str(a) + str(b))
    
    calibrationTotal = 0
    for line in lines:
        eq = line.split(":")
        result = int(eq[0])
        operands = eq[1].strip().split(" ")
        print(line)
        operators = []
        perms = list(itertools.product(ops, repeat=len(operands)-1))
        for perm in perms:
            total = int(operands[0])
            for index, operator in enumerate(perm):
                total = operate(total,int(operands[index+1]), operator)
                if total > result:
                    break
            if total == result:
                print(f"valid {perm}")
                calibrationTotal += total

                break
    
    print(f"calibrationTotal: {calibrationTotal}")
                