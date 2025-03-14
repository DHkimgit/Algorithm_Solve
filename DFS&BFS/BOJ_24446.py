import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

queue = deque()
depth = 0
visited[R] = depth
queue.append((R, depth))

while queue:
    point, depth = queue.popleft()
    for next_point in graph[point]:
        if visited[next_point] != -1:
            continue
        queue.append((next_point, depth + 1))
        visited[next_point] = depth + 1

for i in range(1, N + 1):
    print(visited[i])
