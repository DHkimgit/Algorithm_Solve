T = int(input())
for i in range(T):
    N = int(input())
    dp = [1 for x in range(N + 2)]
    if N < 3:
        print(dp[N-1])
        continue
    else:
        for j in range(3, N + 1):
            dp[j] = dp[j - 3] + dp[j - 2]
        print(dp[N-1])
        continue
    