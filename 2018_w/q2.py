

def parse_text(text):
    var_s = 0
    var_t = 0
    idx = 0
    while idx < len(text)-1:
        letter = text[idx]
        if letter == 'S':
            var_s += 1
            idx += 1
        elif letter == 's':
            var_s -= 1
            idx += 1
        elif letter == 'T':
            var_t += 1
            idx += 1
        elif letter == 't':
            var_t -= 1
            idx += 1
        elif letter == 'f':
            idx = len(text)
        elif letter == 'j':
            idx = int(text[idx+1:idx+5]) - 1  # 番目とindexを合わせる
        elif letter == 'b':
            if var_s > 0:
                idx = int(text[idx+1:idx+5]) - 1
            else:
                idx += 5

    return var_s, var_t

# text = 'SSSSj0013ssTb0010f'
text = input()
print(parse_text(text))