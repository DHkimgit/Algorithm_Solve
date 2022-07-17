K = int(input())

S = []
result = 0

for i in range(K):
    tmp = int(input())
    if tmp != 0:
        S.append(tmp)
    else:
        S.pop()

for i in range(len(S)):
    result += S[i]

print(result)