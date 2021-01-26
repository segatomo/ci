
def root(x):
    x = float(x)
    right = x
    left = 0.0
    esp = 1e-7
    while abs(left - right) > esp:
        mid = (right + left) / 2
        if (mid * mid > x):
            right = mid
        else:
            left = mid
    return right

def solve6():
    return (1+root(5))/2.0


if __name__ == "__main__":
    print(solve6())