def find_duplicate(text):
    printed = []   # すでに表示した行を記録しておく 
    idx = 0
    while idx < len(text)-1:
        if text[idx] in printed:
            idx += 1
        elif text[idx] == text[idx+1]:
            if text[idx] == text[idx+2]:
                if text[idx] == text[idx+3]:
                    print(text[idx])
                    printed.append(text[idx])
                    idx += 4
                else:
                    idx += 3
            else:
                idx += 2
        else:
            idx += 1
            

if __name__ == "__main__":
    text = []
    with open('program1.txt') as f:
        for line in f.readlines():
            text.append(line.split('\n')[0])
    find_duplicate(text)