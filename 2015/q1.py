def count_semicolon(text):
    cnt = 0
    for t in text:
        if ";" in t:
            cnt += 1
    return cnt

if __name__ == "__main__":
    text = []
    with open('program.txt') as f:
        for line in f.readlines():
            text.append(line)
    print("セミコロンの個数: {}".format(count_semicolon(text)))