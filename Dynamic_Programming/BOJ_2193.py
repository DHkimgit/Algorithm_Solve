# dp[i][j] 에서 dp[1][0] 은 1자리 이친수 중에서 0으로 끝나는 것의 개수, dp[1][1]은 1자리 이친수 중에서 1로 끝나는 것의 개수
n = int(input())

dp = [[-1, -1] for x in range(n + 1)]
dp[1][0] = 0
dp[1][1] = 1

if n == 1:
    print(1)
else:
    for i in range(2, n + 1):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-1][0]

    print(dp[n][1] + dp[n][0])
