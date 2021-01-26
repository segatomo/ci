import numpy as np
label = list(map(str, range(1,10))) + ["0"] \
              + list(map(chr, range(65, 91)))

              
def calc_depth(filename, debug=False):
    tiles = []
    with open(filename) as f:
        tiles = list(map(int, list(f.readline())))
    square = np.zeros((1, 10))
    availabel_x_history = [-1]*len(tiles)
    for num, t in enumerate(tiles):
        if debug:
            print('\n-------{}-{}--------\n'.format(num+1, t))
        # 0がtこ以上続いている行を見つける
        # そこから必要な分だけ行を増やす
        availabel_x = 0   # 入れられる場所の左上の列index
        availabel_y = 0   # 入れられる場所の左上の行index
        flagx = False
        flagy = False
        for j, row in enumerate(square):
            x_space = 0
            for i, n in enumerate(row):
                if n == 0 and x_space == 0:
                    x_space += 1
                    availabel_x = i 
                elif n == 0:
                    x_space += 1
                else:
                    x_space = 0
                if x_space == t:
                    flagx = True
                    # tが入るスペースが見つかったらやめる
                    if sum(square[j:j+t, availabel_x]) == 0:
                        availabel_y = j
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
        availabel_x_history[num] = availabel_x
        if len(square) - availabel_y < t:
            square = np.append(square, np.zeros((t-len(square)+availabel_y, 10)), axis=0).copy()
        if availabel_x_history[num-1]+t > 10:
            square[availabel_y:availabel_y+t, 0:t] = num+1
        else:
            square[availabel_y:availabel_y+t, availabel_x:availabel_x+t] = num+1
        if debug:
            print(square)
    return square

if __name__ == "__main__":
    import glob
    files = glob.glob('tile3*')
    print(label)
    for file_name in files:
        res = calc_depth(file_name)
        ans = []
        for row in res:
          line = []
          for num in row:
            if num == 0:
              line.append(" ")
            else:
              line.append(label[int(num-1)])
          ans.append(line)
        import pprint
        print("\n----{}の配置結果----".format(file_name))
        # print(res)
        pprint.pprint(ans)