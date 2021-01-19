import random
from itertools import product

def parse_text(text):
    var_s = 0
    var_t = 0
    num_list = []
    idx = 0
    instructions = []
    while idx < len(text)-1:
        letter = text[idx]
        # print(letter)
        instructions.append(letter)
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
            rand = random.random()
            if rand > 0.5:
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

    return var_s, var_t, instructions

def count_instruction(text):
    """
    textから命令の数(=英字の数)を数える
    """
    ans = 0
    for letter in list(text):
        if letter.isalpha():
            ans += 1
    return ans

# b○○○○は1/2の確率でどちらかの動作をする
# 2^92とかはやばいから全通りみるのは現実的ではない
# b○○○○の○○○○の最大のインデックスが表す数字の直後にあるfより後ろにある命令は実行されないのでは

def count_b(text):
    cnt = 0
    for letter in list(text):
        if letter == 'b':
            cnt += 1
    return cnt

with open('prog6.txt') as f:
    text = f.readline()

instruction_count = count_instruction(text)
tmp = instruction_count
for i in range(1000000):
    # print(i, end='')
    s, t, instructions = parse_text(text)
    if len(instructions) < tmp:
        tmp = len(instructions)
print(tmp)