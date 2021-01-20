def find_main(text):
    for i, t in enumerate(text):
        if "main" in t:
            print("行番号: {}".format(i))
            print("mainを含む行: {}".format(t))

if __name__ == "__main__":
    text = []
    with open('program.txt') as f:
        for line in f.readlines():
            text.append(line.split('\n')[0])
    find_main(text)