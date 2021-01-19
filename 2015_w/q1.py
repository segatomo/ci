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

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    print(f(100))