def g(n):
    """
    >>> g(2)
    29785766
    >>> g(3)
    41857255
    """
    if n < 0:
        return 1
    else:
        mod = 2**26
        data = [1]
        for i in range(1,n+1):
            data.append((1103515245*data[i-1]+12345)%mod)
        return data[n]

def find_k(n):
    gn = g(n)
    flag = False
    k = 1
    data = [gn]
    while flag == False:
        data.append((1103515245*data[k-1]+12345)%2**26)
        if  data[k] == gn:
            flag = True
        else:
            k += 1
            if k%10000000 == 0:
                print(k)
    return k


def h(n):
    return g(n)%2**10

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    # print(g(2))
    # print(g(3))
    # print(find_k(2))
    print(find_k(3))