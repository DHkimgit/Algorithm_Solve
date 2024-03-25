n = int(input())
end = 2*n - 1
mid = end // 2

for i in range(1, end + 1):
    if i <= mid:
        for j in range(i):
            print("*", end='')
        for k in range(2*n - 2*i):
            print(" ", end='')
        for l in range(i):
            if l == i-1:
                print("*")
            else:
                print("*", end='')

    elif i == mid + 1:
        for i in range(end + 1):
            if i == end:
                print("*")
            else:
                print("*", end='')
    
    else:
        for j in range(2*n - i):
            print("*", end='')
        for k in range(2*i - 2*n):
            print(" ", end='')
        for l in range(2*n - i):
            if l == 2*n - i-1:
                print("*")
            else:
                print("*", end='')
