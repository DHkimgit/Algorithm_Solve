a, b = map(int, input().split())
reversed_a = int(str(a)[::-1])
reversed_b = int(str(b)[::-1])
if reversed_a > reversed_b:
    print(reversed_a)
else:
    print(reversed_b)
