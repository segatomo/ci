def f(n):
    """
    >>> f(2)
    2618
    >>> f(1)
    1
    """
    mod = 2**24
    if n < 1:
        return 1
    else:
        data = [1]
        for i in range(1,n+1):
            data.append((161*data[i-1]+2457)%mod)
        return data[n]

def count_even():
    cnt = 0
    for i in range(100):
        if f(i) % 2 == 0:
            cnt += 1
    return cnt

def count_odd():
    cnt = 0
    for i in range(100):
        if f(i) % 2 == 1:
            cnt += 1
    return cnt


if __name__ == "__main__":
    print(count_even())
    print(count_odd())
    print(f(1000000))