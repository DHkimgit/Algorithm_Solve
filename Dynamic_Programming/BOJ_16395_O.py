n, k = map(int, input().split())

      
def factorial(k):
    l = 1
    for i in range(2, k+1):
        l *= i
    return l

def solve(n, k):
    ans = factorial(n) // factorial(k) // factorial(n-k)
    return ans

print(solve(n-1, k-1))

# 파스칼의 삼각형