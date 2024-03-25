n = int(input())
k = list(map(int, input().split()))
dp = [0 for x in range(n)]

# dp[i] = 배열의 i번째를 가장 큰 수로 하는 가장 큰 증가하는 부분수열의 길이

for i in range(0, n):
    dp[i] = 1
    for j in range(0, i):
        if k[j] <= k[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))