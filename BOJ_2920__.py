k = list(map(int, input().split()))


if k[0] == 1:
    stack = 0
    for i in range(0, len(k) - 1):
        if k[i] + 1 == k[i+1]:
            stack += 1
        else:
            print("mixed")
            break
    if stack == 7:
        print("ascending")
    
elif k[0] == 8:
    stack = 0
    for i in range(0, len(k) - 1):
        if k[i] - 1 == k[i+1]:
            stack += 1
        else:
            print("mixed")
            break
    if stack == 7:
        print("descending")

else:
    print("mixed")