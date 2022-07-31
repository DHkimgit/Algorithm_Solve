A, B = map(int, input().split())

def XOR(n):
    div4 = n % 4
    if div4 == 0:
        return n
    if div4 == 1:
        return 1
    if div4 == 2:
        return n + 1
    return 0

print(XOR(A - 1) ^ XOR(B))