# 2.6
A = [1, 2, 3, 4, 5]

for i in range(-1, -len(A) - 1, -1):
    print("value = ", A[i], end="")
    print(" index = ", i)

# 2.7
def sum_list(target : list[int]):
    result = 0
    for i in target:
        result += i
    return result

print(sum_list(A))

# 2.8
msg = "Data Structure in Python"
print(msg)
print(msg.upper())
print(msg.lower())

# 2.9.1
price = {'콩나물해장국': 4500, '갈비탕':9000, '돈가스':8000}
price['팟타이'] = 7000
print(price.keys())
print(price.values())
print(price)

# 2.9.2
for i in price.keys():
    price[i] -= 500
print(price)

# 2.10
def hamonic_iter(n : int):
    result = 0.0
    for i in range(1, n + 1):
        result += 1.0 / i
    return result

def hamonic_recur(n : int):
    result = 0.0
    result += hamonic_iter(n - 1) + 1.0/n
    return result

print(hamonic_iter(15))
print(hamonic_recur(15))

# 2.11
def binomial_recur(n: int, k: int):
    if k == 0 or k == n:
        return 1
    if 0 < k < n:
        return binomial_recur(n-1, k-1) + binomial_recur(n-1, k)

def binomial_iter(n: int, k: int) -> int:
    # n이 k보다 작으면 0을 반환
    if k > n:
        return 0
    
    # 이항계수를 저장할 2차원 리스트 초기화
    C = [[0] * (k + 1) for _ in range(n + 1)]
    
    # C(n, 0) = 1, C(n, n) = 1
    for i in range(n + 1):
        C[i][0] = 1  # C(n, 0) = 1
        if i <= k:
            C[i][i] = 1  # C(n, n) = 1
    
    # Bottom-Up 방식으로 이항계수 계산
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    
    return C[n][k]


print(binomial_recur(7, 2))
print(binomial_iter(7, 2))

# 2.12
def reverse(target: str) -> str:
    result = []
    for i in range(len(target) - 1, -1, -1):
        result.append(target[i])
    return ''.join(result)

print(reverse("ABCDE"))

# 2.13
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)


