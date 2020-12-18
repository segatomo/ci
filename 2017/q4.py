import numpy as np

digits = {
    0: np.array([
        ["*","*","*","*"],
        ["|"," "," ","|"],
        ["*"," "," ","*"],
        ["|"," "," ","|"],
        ["*","*","*","*"],
        ]).T,
    1: np.array([
        ["*"],
        ["|"],
        ["*"],
        ["|"],
        ["*"]]).T,
    2:np.array([
        ["*","*","*","*"],
        [" "," "," ","|"],
        ["*","*","*","*"],
        ["|"," "," "," "],
        ["*","*","*","*"]]).T,
    3: np.array([
        ["*","*","*","*"],
        [" "," "," ","|"],
        ["*","*","*","*"],
        [" "," "," ","|"],
        ["*","*","*","*"]
    ]).T,
    4: np.array([
        ["*"," "," ","*"],
        ["|"," "," ","|"],
        ["*","*","*","*"],
        [" "," "," ", "|"],
        [" "," "," ", "*"],
    ]).T,
    5: np.array([
        ["*","*","*","*"],
        ["|"," "," "," "],
        ["*","*","*","*"],
        [" "," "," ","|"],
        ["*","*","*","*"],
    ]).T,
    6: np.array([
        ["*"," "," "," "],
        ["|"," "," "," "],
        ["*","*","*","*"],
        ["|"," "," ","|"],
        ["*","*","*","*"],
    ]).T,
    7: np.array([
        ["*","*","*","*"],
        [" "," "," ", "|"],
        [" "," "," ", "*"],
        [" "," "," ", "|"],
        [" "," "," ", "*"],
    ]).T,
    8: np.array([
        ["*","*","*","*"],
        ["|"," "," ","|"],
        ["*","*","*","*"],
        ["|"," "," ","|"],
        ["*","*","*","*"],
    ]).T,
    9: np.array([
        ["*","*","*","*"],
        ["|"," "," ","|"],
        ["*","*","*","*"],
        [" "," "," ", "|"],
        [" "," "," ", "*"],
    ]).T
}

def is_equal(mat_a, mat_b):
    """
    2次元配列同士が同じか判定
    """
    for i in range(len(mat_b)):
        if mat_a.shape == mat_b.shape:
            if not all(mat_a[i] == mat_b[i]):
                return False
        else:
            return False
    return True

def get_keys_from_value(d, val):
    for k,v in d.items():
        if is_equal(v, np.array(val)):
            return k

data = []
ans = []
with open('out3.txt') as f:
    for i, l in enumerate(f.readlines()):
        data.append([s for s in list(l) if s!='\n'])
data = np.array(data).T
# print(data)
digit_list = []
digit = []
for line in data:
    if not all(line == " "):
        digit.append(list(line))
    else:
        if digit != []:
            digit_list.append(digit)
        digit = []
digit_list.append(digit)
digit_list_refine = []
for d in digit_list:
    start_index = 0
    for i, letter in enumerate(d[0]):
        if letter == "*":
            start_index = i
            break
    if len(d) > 1:
        digit_list_refine.append([
            d[0][start_index:start_index+5],
            d[1][start_index:start_index+5],
            d[2][start_index:start_index+5],
            d[3][start_index:start_index+5]
        ])
    else:
        digit_list_refine.append([
            d[0][start_index:start_index+5]
        ])
ans = [get_keys_from_value(digits, d) for d in digit_list_refine]
print(''.join(list(map(str, ans))))