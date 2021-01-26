filename = "tile4a.txt"
tiles = []
with open(filename) as f:
    tiles = list(map(int, list(f.readline())))
sort_tiles = sorted(tiles, reverse=True)
print(sort_tiles)
# for t in sort_tiles:
