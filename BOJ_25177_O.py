N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
plusScore = 0
c = []
if (len(a) == len(b)):
    for i in range(N):
        c.append(b[i] - a[i])
    if(max(c)>=0):
        plusScore = max(c)
    else:
        plusScore = 0
    
elif (len(a) > len(b)):
    for i in range(M):
        c.append(b[i] - a[i])
    if(max(c)>=0):
        plusScore = max(c)
    else:
        plusScore = 0
else: 
    for i in range(N):
        c.append(b[i] - a[i])
    for i in range(M-N):
        c.append(b[i+N])
    if(max(c)>=0):
        plusScore = max(c)
    else:
        plusScore = 0

print(plusScore)