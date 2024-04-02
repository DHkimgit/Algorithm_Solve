T = int(input())
result = []
dp = [-1] * 41
zero = [0] * 41
one = [0] * 41

zero[0] = 1
one[1] = 1

def fibo(n):
    if n == 0 or n == 1:
        return

    for i in range(2, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]
        zero[i] = zero[i - 1] + zero[i - 2]
        one[i] = one[i - 1] + one[i - 2]

for i in range(T):
    N = int(input())

    fibo(N)

    print(zero[N], one[N])
