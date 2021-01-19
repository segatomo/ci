from operator import le
import random
import numpy as np
from numpy.core.defchararray import join

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
    num_list = []

    for letter in list(text):
        if letter.isalpha():
            ans += 1
        elif letter.isdigit():
            num_list.append(letter)

    return ans, num_list

# b○○○○は1/2の確率でどちらかの動作をする
# 全通りみる
# 2^92とかはやばい

def count_b(text):
    cnt = 0
    for letter in list(text):
        if letter == 'b':
            cnt += 1
    return cnt

with open('prog5.txt') as f:
    text = f.readline()

instruction_count, num_list = count_instruction(text)
num_list_split = np.array_split(num_list, len(num_list)/4)
print(instruction_count)
num_list_final = [int("".join(l)) - 1 for l in num_list_split]
max_num = max(num_list_final)
print(max_num)
# 絶対に実行されない命令→○○○○の最大の数字の直後のfより後の命令
def find_last_f_idx(text, max_num):
    for i, letter in enumerate(list(text)[max_num:]):
        print(letter)
        if letter == 'f':
            return i

last_f = find_last_f_idx(text, max_num)
print(last_f)