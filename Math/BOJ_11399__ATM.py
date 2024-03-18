N = int(input())
p = list(map(int, input().split()))
result = 0
p.sort()

for i in range(len(p)+1):
    tmp = 0
    for j in range(0, i):
        tmp += p[j]
    result += tmp

print(result)