T = int(input())
array = [[] for _ in range(T)]
for i in range(T):
    tmp = list(map(str, input().split()))
    for j in range(len(tmp)):
        array[i].append(tmp[j][::-1])

for i in range(T):
    print(*array[i])
