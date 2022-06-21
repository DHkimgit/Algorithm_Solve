N, K = map(int, input().split())
L = []

for i in range(3, K-1):
    if(N%i == 0):
        L.append(i)

if(len(L) == 2):
    if(L[0] > K and L[1] > K):
        print('GOOD')
    else:
        if(L[0] < L[1]):
            print('BAD', L[0])
        else:
            print('BAD', L[1])
