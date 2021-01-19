import numpy as np
tiles = []
with open('tile2a.txt') as f:
    tiles = list(map(int, list(f.readline())))
square = np.zeros((1, 10))
start = (0,0)   # 空いている一番上左のマス目
for t in tiles:
    print('\n-------{}--------\n'.format(t))
    # 0がtこ以上続いている行を見つける
    # そこから必要な分だけ行を増やす
    available_x = 0   # 入れられる場所の左上の列index
    available_y = 0   # 入れられる場所の左上の行index
    flag = False
    for j, row in enumerate(square):
        x_space = 0
        y_space = 0
        for i, n in enumerate(row):
            if n == 0 and x_space == 0:
                x_space += 1
                available_x = i
            elif n == 0:
                x_space += 1
            else:
                x_space = 0
            if x_space == t:
                # tが入るスペースが見つかったらやめる
                if sum(square[j:j+t+1, available_x]) == 0:
                    available_y = j
                    flag = True
        if flag:
            break
    if len(square) - available_y < t:
        square = np.append(square, np.zeros((t-len(square)+available_y, 10)), axis=0).copy()
    if available_x+t > 10:
        square[available_y:available_y+t, 0:t] = t
    else:
        square[available_y:available_y+t, available_x:available_x+t] = t
    print(square, available_x, available_y)