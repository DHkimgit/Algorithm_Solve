N, K = map(int, input().split())

weight = [0 for x in range(N + 1)]
value = [0 for x in range(N + 1)]

dp = [[0 for x in range(K+1)] for x in range(N + 1)]

for i in range(N):
    wi, vi = map(int, input().split())
    weight[i] = wi
    value[i] = vi

for i in range(N+1):
    for w in range(K + 1):
        if i == 0 or w == 0:
            dp[i][w] = 0
        elif weight[i - 1] <= w:
            dp[i][w] = max(value[i-1] + dp[i-1][w - weight[i-1]], dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]

print(dp[N][K])