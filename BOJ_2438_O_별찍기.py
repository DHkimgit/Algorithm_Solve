N = int(input())

for i in range(1, N+2):
    for j in range(1, i):
        if j == i-1:
            print("*")
        else:
            print("*", end='')