x = int(input())

dp = [0] * 30001

for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1