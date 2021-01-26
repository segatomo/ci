from os import EX_DATAERR


dic = {}
strings = list(map(chr, range(65, 91))) \
    + list(map(str.lower, list(map(chr, range(65, 91))))) \
    + list(map(str, range(10))) + ["@", "#"]
for i in range(64):
    dic[strings[i]] = bin(i)[2:].zfill(6)

def parse_text(filename):
    """
    テキストファイルからバイナリファイルに変換する
    """
    with open(filename) as f:
        line = f.readline()
    bitarray = []
    for i in range(len(line)):
        bitarray.append(dic[line[i]])
    print(''.join(bitarray))

if __name__ == "__main__":
    parse_text("data1.txt")
# with open('data1.txt') as f:
#     bit_array = f.read()
# print(bit_array[310:321])