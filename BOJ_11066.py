T = int(input())
Array = [[] for _ in range(T)]
print(Array)
for i in range(T):
    K = int(input())
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        Array[i].append(tmp[j])
    Array[i].sort()

print(Array)