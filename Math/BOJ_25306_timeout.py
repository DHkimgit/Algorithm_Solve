from operator import xor
A, B = map(int, input().split())

def XOR(x, y):
    return x^y

array = []
array.append(XOR(A, A+1))
for i in range(B - A):
    if A == B - 1:
        break
    array.append(XOR(array[i], A + 2))
    A += 1
print(array[-1])
