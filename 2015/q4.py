def print_duplicate(text):
    duplicate = []   # 重複している行
    read_text = []   # 読み終わった行
    for t in text:
        if t in read_text:
            if not t in duplicate:
                print(t)
                duplicate.append(t)
        else:
            read_text.append(t)
    print("重複している行の総数: {}".format(len(duplicate)))

if __name__ == "__main__":
    text = []
    with open('sample.txt') as f:
        for line in f.readlines():
            text.append(line.split('\n')[0])
    print_duplicate(text)