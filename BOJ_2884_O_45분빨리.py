a, b = map(int, input().split())

b1 = b - 45
if b1 >= 0:
    print(a, b1)
else:
    b2 = 15 + b
    a1 = a - 1
    if a1 >= 0:
        print(a1, b2)
    else:
        print(23, b2)
