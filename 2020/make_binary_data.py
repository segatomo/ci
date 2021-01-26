import random
with open('data1.txt', mode='w') as f:
    for _ in range(480):
        i = random.random()
        f.write(str(round(i)))

with open("sample.txt") as f:
    nums = f.readline().split(" ")
with open("sample.bin", mode="w") as f:
    for i in range(len(nums)):
        f.write(str(int(nums[i], 16)))