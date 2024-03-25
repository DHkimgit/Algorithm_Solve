n = int(input())
k = list(map(int, input().split()))
dp_LIS = [0 for x in range(n)]
dp_LDS = [0 for x in range(n)]
dp = [0 for x in range(n)]
# dp[i] = 배열의 i번째를 가장 큰 수로 하는 가장 큰 증가하는 부분수열의 길이

for i in range(0, n):
    dp_LIS[i] = 1
    for j in range(0, i):
        if k[j] <= k[i]:
            dp_LIS[i] = max(dp_LIS[i], dp_LIS[j] + 1)

for i in range(0, n):
    dp_LDS[i] = 1
    for j in range(0, i):
        if k[j] >= k[i]:
            dp_LDS[i] = max(dp_LDS[i], dp_LDS[j] + 1)
# 증가 찾기
for i in range(0, n):
    stack = 0
    for j in range(i+1, n):
        if k[j-1] <= k[j]:
            stack += 1
        else:
            break
    dp[i] = stack



print(dp_LIS)
print(dp_LDS)
print(dp)
