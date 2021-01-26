import math
def calc(x):
    res = [1, 1] + [0]*(x-2)
    for i in range(2, x):
        res[i] = res[i-1]+res[i-2]
    return res[x-1]
    

if __name__ == "__main__":
    print(calc(140))
    print(str(calc(140)).zfill(32))