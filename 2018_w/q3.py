

def parse_text(text):
    var_s = 0
    var_t = 0
    num_list = []
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
        elif letter == 'c':
            num_list.append(int(text[idx+1:idx+5]))
            idx += 5
        elif letter == 'r':
            print("pop {}".format(num_list[-1]))
            idx = num_list[-1] - 1
            num_list = num_list[:-1]

    return var_s, var_t

text = 'c0007fSSttr'
print(parse_text(text))