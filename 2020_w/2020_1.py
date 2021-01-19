tiles = []
with open('tile1.txt') as f:
    tiles = list(map(int, list(f.readline())))
depth = 0
flag = False   # 隙間があるか
for t in tiles:
    if t == 2:
        depth += 2
    else:
        if flag == True:
            flag = False
        else:
            depth += 1
            flag = True
print(depth)