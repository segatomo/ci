import random
with open('data1.txt', mode='w') as f:
    for _ in range(480):
        i = random.random()
        f.write(str(round(i)))