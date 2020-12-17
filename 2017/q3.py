digits = {
    0: [
        ["*","*","*","*"],
        ["|"," "," ","|"],
        ["*"," "," ","*"],
        ["|"," "," ","|"],
        ["*","*","*","*"],],
    1: [
        ["*"],
        ["|"],
        ["*"],
        ["|"],
        ["*"]],
    2:[
        ["*","*","*","*"],
        [" "," "," ","|"],
        ["*","*","*","*"],
        ["|"," "," "," "],
        ["*","*","*","*"]],
    3: [
        ["*","*","*","*"],
        [" "," "," ","|"],
        ["*","*","*","*"],
        [" "," "," ","|"],
        ["*","*","*","*"]
    ],
    4: [
        ["*"," "," ","*"],
        ["|"," "," ","|"],
        ["*","*","*","*"],
        [" "," "," ", "|"],
        [" "," "," ", "*"],
    ],
    5: [
        ["*","*","*","*"],
        ["|"," "," "," "],
        ["*","*","*","*"],
        [" "," "," ","|"],
        ["*","*","*","*"],
    ],
    6: [
        ["*"," "," "," "],
        ["|"," "," "," "],
        ["*","*","*","*"],
        ["|"," "," ","|"],
        ["*","*","*","*"],
    ],
    7: [
        ["*","*","*","*"],
        [" "," "," ", "|"],
        [" "," "," ", "*"],
        [" "," "," ", "|"],
        [" "," "," ", "*"],
    ],
    8: [
        ["*","*","*","*"],
        ["|"," "," ","|"],
        ["*","*","*","*"],
        ["|"," "," ","|"],
        ["*","*","*","*"],
    ],
    9: [
        ["*","*","*","*"],
        ["|"," "," ","|"],
        ["*","*","*","*"],
        [" "," "," ", "|"],
        [" "," "," ", "*"],
    ]
}

def calc_width(nums):
    """
    inputされた文字列から幅を求める
    """
    num = nums[0]
    res = 0
    for n in num:
        if n == 1:
            res += 1
        else:
            res += 4
    nums = list(map(int, nums))
    return res+sum(nums[2:][::2])

nums = input().split(',')
num = nums[0]
hspace = list(map(int, nums[1:][::2]))
wspace = list(map(int, nums[2:][::2]))
width = calc_width(nums)
res = [0]*(max(hspace)+5)
for i in range(max(hspace)+5):
    # i:行番号
    res[i] = []
    for j, n in enumerate(list(num)):
        # j:描く数字の順番
        if j < len(num)-1:
            if i >= hspace[j] and i <= hspace[j]+4:
                # 描く行の時
                res[i].extend(digits[int(n)][i-hspace[j]])
            else:
                # 描かない行の時
                if int(n) == 1:
                    res[i].extend([" "]*1)
                else:
                    res[i].extend([" "]*4)
            res[i].extend([" "]*wspace[j])
        else:
            if i >= hspace[j] and i <= hspace[j]+4:
                # 描く行の時
                res[i].extend(digits[int(n)][i-hspace[j]])
            else:
                # 描かない行の時
                if int(n) == 1:
                    res[i].extend([" "]*1)
                else:
                    res[i].extend([" "]*4)
[print(''.join(r)) for r in res]
with open('out3.txt', mode='w') as f:
    for r in res[:-1]:
        f.write(''.join(r))
        f.write('\n')
    f.write(''.join(res[-1]))
f.close()