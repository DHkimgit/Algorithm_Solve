k = list(map(int, input().split()))

if k[0] == k[1] and k[1] == k[2]:
    print(10000 + 1000 * k[0])
elif k[0] != k[1] and k[0] != k[2] and k[1] != k[2]:
    print(max(k) * 100)
else:
    if k[0] == k[1]:
        print(1000 + 100*k[0])
    else:
        if k[0] == k[2]:
            print(1000 + 100*k[0])
        else:
            print(1000 + 100*k[1])