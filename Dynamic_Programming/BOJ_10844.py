# dp[i][j]는 길이가 i인 수에서 끝부분이 j로 끝나는 계단 수의 개수
# dp[1][j]는 01, 02, ..., 09로 총 9개
# dp[2][0]는 끝이 0로 끝나는 2자리 계단수로서 10이 있는데 이는 dp[1][1] 이다.
# dp[2][1]는 끝이 1로 끝나는 2자리 계단수로서 01과 21 2개가 있는데 dp[1][0] + dp[1][2] 이다
# dp[2][2]는 끝이 2로 끝나는 2자리 계단수로서 12와 31이 있는데 이는 dp[1][1] + dp[1][3] 이다.
# dp[2][9]는 끝이 9로 끝나는 2자리 계단수로서 89이 있는데 이는 dp[1][8] 이다.

n = int(input())

dp = [[0 for x in range(10)] for x in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1

if n == 1:
    print(sum(dp[1]))
else:
    for i in range(2, n+1):
        for j in range(0, 10):
            if j == 0:
                dp[i][j] = dp[i-1][1]
                continue
            if j == 9:
                dp[i][j] = dp[i-1][8]
                continue
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    print(sum(dp[n]) % 1000000000)