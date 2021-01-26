import numpy as np

def parse_txt(filename):
    with open(filename) as f:
        line = f.readline().split(".")[0]
    line = line.split(',')
    mat = []
    for l in line:
        mat.append(list(map(int, (l.split(' ')))))
    return mat

def solve3():
    mat1 = parse_txt("mat1.txt")
    mat2 = parse_txt("mat2.txt")
    c = np.dot(np.array(mat1),np.array(mat2))
    ans = 0
    for i in range(len(c)):
        ans += c[i][i]
    return ans


def solve4(m,n,s):
    cnt = 0
    cache = [(-1,-1)]*s
    for i in range(m):
        for j in range(m):
            for k in range(n):
                # 古いデータがキャッシュアレイの後ろに来るようにする
                if (i,k) in cache:
                    idx = cache.index((i,k))
                    tmp = cache[:idx] + cache[idx+1:]
                    cache[0] = (i,k)
                    cache[1:] = tmp
                else:
                    tmp = cache[:s-1]
                    cache[0] = (i,k)
                    cache[1:] = tmp
                    cnt += 1
                if (k,j) in cache:
                    idx = cache.index((k,j))
                    tmp = cache[:idx] + cache[idx+1:]
                    cache[0] = (i,k)
                    cache[1:] = tmp
                else:
                    tmp = cache[:s-1]
                    cache[0] = (k,j)
                    cache[1:] = tmp
                    cnt += 1       
    return cnt


def check5(m,n,p):
    a = [[1,2,3,4,5,6],
        [2,3,4,5,6,7],
        [3,4,5,6,7,8]]
    b = [[1,2,3],
        [2,3,4],
        [3,4,5],
        [4,5,6],
        [5,6,7],
        [6,7,8]]
    c = [[0]*m]*m
    for u in range(0,m//p,p):
        for v in range(0,m//p,p):
            for w in range(0,n//p,p):
                i = u
                for i in range(u+p):
                    j = v
                    for j in range(v+p):
                        d = 0
                        k = w
                        for k in range(w+p):
                            d += a[i][k] * b[k][j]
                        c[i][j] += d
    return c

if __name__ == "__main__":
    # mat = parse_txt("mat1.txt")
    # print("行の数: {}, 列の数: {}".format(len(mat), len(mat[0])))
    # print("対角成分の和: {}".format(solve3()))
    # print(solve4(3,4,48))
    print(check5(6,3,3))
    print(np.dot(
        np.array([[1,2,3,4,5,6],
        [2,3,4,5,6,7],
        [3,4,5,6,7,8]]),
        np.array([[1,2,3],
        [2,3,4],
        [3,4,5],
        [4,5,6],
        [5,6,7],
        [6,7,8]]),
    ))