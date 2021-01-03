with open('prog1.txt') as f:
    lines = f.readlines()
operands = [l.strip('\n').split(' ')[1] for l in lines]
[print(o) for o in operands]