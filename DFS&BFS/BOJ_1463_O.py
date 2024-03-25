from collections import deque

N = int(input())

queue = deque()
queue.append(N)
graph = [99999 for x in range(N + 1)]
graph[N] = 0

while queue:
    x = queue.popleft()
    queue.append(x - 1)
    if x == 0:
        break
    graph[x - 1] = min(graph[x] + 1, graph[x - 1])

    if x % 2 == 0:
        queue.append(x//2)
        graph[x//2] = min(graph[x//2], graph[x] + 1)
    if x % 3 == 0:
        queue.append(x//3)
        graph[x//3] = min(graph[x//3], graph[x] + 1)

print(graph[1])






# N = int(input())
# dp = [0 for x in range(N + 1)]

# for i in range(2, N+1):
#     dp[i] = dp[i-1] + 1
#     if i%2 == 0:
#         dp[i] = min(dp[i], dp[i//2] + 1)
#     if i%3 == 0:
#         dp[i] = min(dp[i], dp[i//3] + 1)

# print(dp[N])

