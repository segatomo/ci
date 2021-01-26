import numpy as np
def calc_depth(filename, debug=False):
    tiles = []
    with open(filename) as f:
        tiles = list(map(int, list(f.readline())))
    square = np.zeros((1, 10))
    available_x_history = [-1]*len(tiles)
    for num, t in enumerate(tiles):
        if debug:
            print('\n-------{}-{}--------\n'.format(num+1, t))
        # 0がtこ以上続いている行を見つける
        # そこから必要な分だけ行を増やす
        available_x = 0   # 入れられる場所の左上の列index
        available_y = 0   # 入れられる場所の左上の行index
        flagx = False
        flagy = False
        for j, row in enumerate(square):
            x_space = 0
            for i, n in enumerate(row):
                if n == 0 and x_space == 0:
                    x_space += 1
                    available_x = i 
                elif n == 0:
                    x_space += 1
                else:
                    x_space = 0
                if x_space == t:
                    flagx = True
                    # tが入るスペースが見つかったらやめる
                    if sum(square[j:j+t, available_x]) == 0:
                        available_y = j
                        flagy = True
                if flagx:
                    break
            if flagy:
                break
        if flagx == False and flagy == False:
            tmp_y = len(square)
            square = np.append(square, np.zeros((t, 10)), axis=0).copy()
            square[tmp_y:tmp_y+t, 0:t] = num+1
            if debug:
                print(square)
            continue
        available_x_history[num] = available_x
        if len(square) - available_y < t:
            square = np.append(square, np.zeros((t-len(square)+available_y, 10)), axis=0).copy()
        if available_x_history[num-1]+t > 10:
            square[available_y:available_y+t, 0:t] = num+1
        else:
            square[available_y:available_y+t, available_x:available_x+t] = num+1
        if debug:
            print(square)
    return len(square)

if __name__ == "__main__":
    import glob
    files = glob.glob('tile2*')
    for file_name in files:
        print("{}の配置結果の深さ: {}".format(file_name, calc_depth(file_name)))