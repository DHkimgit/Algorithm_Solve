import time

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-2) + fib(n-1)

def fib_iter(n):
    s = [0, 1]
    for i in range(2, n+1): 
        s.append(s[i-1] + s[i-2])
    return s[-1]

for i in range(1, 40):
    iter_start_time = time.time()
    fib_iter(i)
    iter_time = time.time() - iter_start_time

    recur_start_time = time.time()
    fib(i)
    recur_time = time.time() - recur_start_time

    print(f"n = {i:<2d}  반복: {iter_time:.20f}  순환: {recur_time:.20f}")


    
def fib_dp(n):
    dp = [-1] * (n + 1)
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    if dp[n] != -1:
        return dp[n]

    dp[n] = fib_dp(n - 1) + fib_dp(n - 2)
    
    return dp[n]

