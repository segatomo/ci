def calc(x):
    if x <= 2:
        return 1
    else:
        return calc(x-1) + calc(x-2)

if __name__ == "__main__":
    print(calc(50))