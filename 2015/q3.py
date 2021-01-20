def print_duplicate(text):
    idx = 0
    while idx < len(text):
        if text[idx] == text[idx+1]:
            print(text[idx])
            idx += 2
        else:
            idx += 1

if __name__ == "__main__":
    text = []
    with open('program.txt') as f:
        for line in f.readlines():
            text.append(line.split('\n')[0])
    print_duplicate(text)