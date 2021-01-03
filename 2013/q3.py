with open('prog1.txt') as f:
    lines = f.readlines()
flag = False
idx = 0
x, y = 0, 0
while flag == False:
    line = lines[idx]
    instruction = line.strip('\n').split(' ')[0]
    opr1 = line.strip('\n').split(' ')[1]
    opr2 = line.strip('\n').split(' ')[2]
    if instruction == 'ADD':
        if opr2 == 'x':
            if opr1 == 'y':
                x += y
            else:
                x += int(opr1)
        elif opr2 == 'y':
            if opr1 == 'x':
                y += x
            else:
                y += int(opr1)
        idx += 1
    # elif instruction == 'CMP':
    #     if opr1 == opr2:
    #         idx += 2
    #     else:
    #         idx += 1
    # elif instruction == 'JMP':
    #     idx += opr1
    elif instruction == 'PRN':
        print(x, y)
        flag = True
    elif instruction == 'SET':
        if opr1 == 'x':
            x = int(opr2)
        elif opr1 == 'y':
            y = int(opr2)
        idx += 1