n = int(input())
k = list(map(int, input().split()))
dp_LIS = [0 for x in range(n)]
dp_LDS = [0 for x in range(n)]

for i in range(0, n):
    if dp_LIS[i - 1] != 1 and i != 0:
        dp_LIS[i] = dp_LIS[i - 1] - 1
    else:
        stack = 0
        for j in range(i + 1, n):
            if k[j-1] <= k[j]:
                stack += 1
            else:
                break
        dp_LIS[i] = stack + 1

for i in range(0, n):
    if dp_LDS[i - 1] != 1 and i != 0:
        dp_LDS[i] = dp_LDS[i - 1] - 1
    else:
        stack = 0
        for j in range(i + 1, n):
            if k[j-1] >= k[j]:
                stack += 1
            else:
                break
        dp_LDS[i] = stack + 1

print(max(max(dp_LIS), max(dp_LDS)))
