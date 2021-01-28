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
board_2[14][4] = gun

values = list(range(3,8)) + list(reversed(range(1,8))) + list(range(1,3))

game_point = 0

for _ in range(3):
    [print(''.join(b)) for b in board_2]
    print()

    # 弾丸の行番号のための変数
    j1 = 1
    j2 = 1
    shot1 = False
    shot2 = False
    for i in range(1,14):
        print(">>> Enter the key")
        key = input()
        print(i, values[i])
        print(14-j1)
        if key == "i":
            if shot1 == False:
                shot1 = True
                new = copy.deepcopy(board_2)
                new[i][values[i]] = target
                if i == 14-j1:
                    # 弾丸が標的に当たったら得点を加算して弾丸と標的は表示しない
                    print("hit1")
                    game_point += 1
                    break
                else:
                    new[14-j1][4] = bullet
                [print(''.join(b)) for b in new]
                print()
            else: 
                if shot2 == False:
                    shot2 = True
                new = copy.deepcopy(board_2)
                new[i][values[i]] = target
                if i == 14-j1 and values[i] == 4:
                    # 弾丸が標的に当たったら得点を加算して弾丸と標的は表示しない
                    print("hit2")
                    game_point += 1
                    break
                else:
                    new[14-j1][4] = bullet
                if i == 14-j2 and values[i] == 4:
                    # 弾丸が標的に当たったら得点を加算して弾丸と標的は表示しない
                    print("hit3")
                    game_point += 1
                    break
                else:
                    new[14-j2][4] = bullet
                [print(''.join(b)) for b in new]
                print()

        elif key == "k":
            new = copy.deepcopy(board_2)
            new[i][values[i]] = target
            if shot1:
                new[14-j1][4] = bullet
            if shot2:
                new[14-j2][4] = bullet
            [print(''.join(b)) for b in new]
            print()
        if shot1:
            j1 += 1
        if shot2:
            j2 += 1