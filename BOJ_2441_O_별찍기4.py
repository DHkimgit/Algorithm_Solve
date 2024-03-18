N = int(input())

for i in range(N+1):
    for j in range(i):
        print(" ", end='')
    for k in range(N-i):
        if k == N-i-1:
            print("*")
        else:
            print("*", end='')
    