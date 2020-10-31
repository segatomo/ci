import math

def parse_txt():
    pixels = []
    with open('image1.txt') as f:
        for line in f:
            p = line.rstrip('\n').split(' ')
            pixels.append([list(map(int, p[i:i+3])) for i in range(0, len(p), 3)])
    return pixels


def no1():
    pixels = parse_txt()
    print(sum([len(p) for p in pixels]))


def no2():
    pixels = parse_txt()
    print(len(pixels[0]))


def sort_pixels():
    pixels = parse_txt()
    data = {}   # 明るさの辞書
    
    width = len(pixels[0])
    for i,l in enumerate(pixels):   # 行ごと
        for j, p in enumerate(l):   # 画素ごと
            data[width*i+j] = sum([v**2 for v in p])
    data_sort = sorted(data.items(), key=lambda x:x[1])
    return data_sort


def no3():
    pixels = parse_txt()
    num = sum([len(p) for p in pixels])
    width = len(pixels[0])
    data_sort = sort_pixels
    idx = data_sort[int(num/2)][0]
    print(pixels[idx//width][idx%width] , idx)


def no4(k):
    pixels = parse_txt()
    num = sum([len(p) for p in pixels])
    width = len(pixels[0])
    data_sort = sort_pixels
    for i in range(k):
        idx = data_sort[int(num*i/k)][0]
        print(pixels[idx//width][idx%width], idx)


def calc_distance(x, y):
    return sum([abs(a-b) for a,b in zip(x,y)])


def clustnum(rep, pixel):
    """
    rep: 代表画素
    pixelがどのクラスタに分類されるか計算する
    """
    res = 0   # クラスタ番号
    tmp = calc_distance(rep[0], pixel)   # 最小距離
    for i in range(1,len(rep)):
        if tmp >= calc_distance(rep[i], pixel):   # 最大のインデックスを選ぶ
            tmp = calc_distance(rep[i], pixel)
            res = i
    return res


def calc_center(c):
    """
    c: １つのクラスタに属するピクセルのリスト
    """
    ans = []
    for i in range(3):
        ans.append(sum([v[i] for v in c])/len(c))
    return ans


def do_clustering(rep, pixels):
    """
    代表画素とピクセルのリストからクラスタリングを実行する
    """
    clust_data = [0]*len(rep)
    for l in pixels:
        for p in l:  # ピクセルごと
            if clust_data[clustnum(rep, p)] == 0:
                clust_data[clustnum(rep, p)] = [p]
            else:
                clust_data[clustnum(rep, p)].append(p)
    return clust_data


def new_rep(centers, pixels):
    """
    中心に一番近いピクセル(=代表ピクセル)のリストを返す
    centers: 中心ピクセルのリスト
    pixels: 全ピクセルのリスト
    """
    rep = [0]*len(centers)
    pixels = sum(pixels, [])
    for j, c in enumerate(centers):
        tmp = calc_distance(c, pixels[0])
        new_center = pixels[0]
        for i in range(1,len(pixels)):
            if tmp >= calc_distance(c, pixels[i]):
                tmp = calc_distance(c, pixels[i]) 
                new_center = pixels[i]
        rep[j] = new_center
    return rep



def no5(k):
    pixels = parse_txt()
    num = sum([len(p) for p in pixels])
    width = len(pixels[0])
    data_sort = sort_pixels()
    rep = []  # 代表画素
    clust_data = []   # クラスタのデータ
    for i in range(k):
        idx = data_sort[int(num*i/k)][0]
        rep.append(pixels[idx//width][idx%width])
        clust_data.append([pixels[idx//width][idx%width]])
    for l in pixels:
        for p in l:  # ピクセルごと
            clust_data[clustnum(rep, p)].append(p)
    rep = [calc_center(c) for c in clust_data]
    for i in range(9):
        clust_data = do_clustering(rep, pixels)
        centers = [calc_center(c) for c in clust_data]
        rep = new_rep(centers=centers, pixels=pixels)
    print(rep)

    


if __name__ == "__main__":
    # print(parse_txt())
    # print('(1)', end='')
    # no1()
    # print('(2)', end='')
    # no2()
    # print('(3)', end='')
    # no3()
    # print('(4)', end='')
    # no4(4)
    print('(5)', end='')
    no5(4)