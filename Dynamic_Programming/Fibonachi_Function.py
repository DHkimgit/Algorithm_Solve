d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

dp = [0] * 100
dp[1] = 1
dp[2] = 2
n = 99

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(fibo(99))
print(dp[98])