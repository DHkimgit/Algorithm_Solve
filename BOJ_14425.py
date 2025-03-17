import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sets = {input().rstrip() for _ in range(n)}
result = 0

for i in range(m):
    target = input().rstrip()
    if target in sets:
        result += 1
print(result)

# T = int(input())

# for i in range(T):
#     n = int(input())
#     s = list(map(int, input().split()))

# def solution(n, s):
#     answer = [0] * n
#     result = 