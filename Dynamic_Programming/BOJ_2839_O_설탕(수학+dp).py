N = int(input())

dp = [0 for x in range(5001)]

dp[3] = 1
dp[5] = 1

def goDown(N):
    if N < 0:
        return 99999

    if dp[N] != 0:
        return dp[N]
    
    if N == 3 or N == 5:
        return 1
    
    dp[N] = min(goDown(N-3) + 1, goDown(N-5) + 1)


for i in range(1, N+1):
    goDown(i)

if dp[N] > 10000:
    print("-1")

else:
    print(dp[N])