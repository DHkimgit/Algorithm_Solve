n = int(input("fibo(n) n값을 입력하세요: "))

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)

def fib_iter(n):
    s = [0, 1]
    for i in range(2, n+1):
        s.append(s[i-1] + s[i-2])
    return s[-1]

print("fib(n) : ", fib(n))
print("fib_iter(n) : ", fib_iter(n))


def fib_dp(n):
    dp = [None] * (n + 1)
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    if dp[n] is not None:
        return dp[n]

    dp[n] = fib_dp(n - 1) + fib_dp(n - 2)
    
    return dp[n]