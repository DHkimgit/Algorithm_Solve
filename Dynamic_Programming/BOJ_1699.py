# https://www.acmicpc.net/problem/1699
# 제곱수의 합 이건 탑다운인가 바텀업인가? 
# dp[i] 는 i를 제곱수의 합으로 나타낼 때 그 제곱수의 항의 최소 개수
import math
n = int(input())
dp = [float('inf')] * (n + 1)
dp[0] = 0

squares = [i*i for i in range(1, int(math.sqrt(n)) + 1)]

for i in range(1, n + 1):
    for square in squares:
        if i < square:
            break
        dp[i] = min(dp[i], dp[i - square] + 1)

print(dp[n])

# 오답 : 그리디로 풀 수 없음. 반례 : 18
# import math
# n = int(input())
# result = 0

# def get_sqrt_num(n: int) -> int:
#     return int(math.sqrt(n))

# while True:
#     i = get_sqrt_num(n)
    
#     if n - i*i == 0:
#         result += 1
#         break
#     else:
#         n -= i*i
#         result += 1

# print(result)