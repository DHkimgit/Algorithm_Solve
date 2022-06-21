import math
N, K = map(int, input().split())
L = []


for i in range(2, K + 1):
    if(N % i == 0):
        L.append(i)
if not L:
    print('GOOD')
else:
    print('BAD', L[0])
