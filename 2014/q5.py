def calc(v1, v2):
    x, a = v1.split()
    y, b = v2.split()
    return float(x)/10**(len(x)-1) * 10**int(a) * float(y)/10**(len(y)-1) * 10**int(b)

if __name__ == "__main__":
    x = '12345678901234567890123456789012 04'
    y = '98765432109876543210987654321098 09'
    print(calc(x,y))