import copy

board = [
    ["|", "-", "-", "-", "-", "-", "-","-", "|"],
    ["|",  " ",  " ",  " ",  " ",  " ",  " ", " ", "|"],
    ["|",  " ",  " ",  " ",  " ",  " ",  " ", " ", "|"],
    ["|",  " ",  " ",  " ",  " ",  " ",  " ", " ", "|"],
    ["|",  " ",  " ",  " ",  " ",  " ",  " ", " ", "|"],
    ["|",  " ",  " ",  " ",  " ",  " ",  " ", " ", "|"],
    ["|",  " ",  " ",  " ",  " ",  " ",  " ", " ", "|"],
    ["|",  " ",  " ",  " ",  " ",  " ",  " ", " ", "|"],
    ["|",  " ",  " ",  " ",  " ",  " ",  " ", " ", "|"],
    ["|",  " ",  " ",  " ",  " ",  " ",  " ", " ", "|"],
    ["|",  " ",  " ",  " ",  " ",  " ",  " ", " ", "|"],
    ["|",  " ",  " ",  " ",  " ",  " ",  " ", " ", "|"],
    ["|",  " ",  " ",  " ",  " ",  " ",  " ", " ", "|"],
    ["|",  " ",  " ",  " ",  " ",  " ",  " ", " ", "|"],
    ["|", ".", ".", ".", ".", ".", ".",".", "|"],
]

point = "v"
gun = "x"
target = "o"
bullet = "e"

board_2 = copy.deepcopy(board)
board_2[0][4] = point
[print(''.join(b)) for b in board_2]
print()

values = list(range(3,8)) + list(reversed(range(1,7))) + list(range(2,5))

for _ in range(3):
    [print(''.join(b)) for b in board_2]
    for i in range(1,14):   # 行
        print(">>> Enter the key")
        key = input()
        if key == "k":
            new = copy.deepcopy(board_2)
            new[i][values[i]] = target
            [print(''.join(b)) for b in new]
            print()