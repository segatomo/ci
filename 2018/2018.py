import numpy as np

def parse(filename):
    with open(filename) as f:
        for line in f:
            # 「.」以降の文字は無視
            res = [list(map(int, l.split(' '))) for l in line.split('.')[0].split(',')]
    return res

def product(a,b):
    c = np.zeros((len(a), len(a)))
    for i in range(len(a)):
        for j in range(len(a)):
            d = 0
            for k in range(len(a[0])):
                d += a[i][k]*b[k][j]
            c[i][j] = d
    return c


if __name__ == "__main__":
    mat = parse('mat1.txt')
    print(np.array(mat).shape)
    mat1 = parse('mat1.txt')
    mat2 = parse('mat2.txt')
    prod = product(mat1, mat2)
    print(sum([prod[i][i] for i in range(len(prod))]))