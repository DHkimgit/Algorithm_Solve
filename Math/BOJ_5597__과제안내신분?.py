table = [0 for x in range(30)]
for i in range(28):
    k = int(input()) - 1
    table[k] = 1
for i in range(30):
    if table[i] != 1: 
        print(i + 1)