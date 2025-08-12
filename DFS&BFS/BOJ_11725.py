from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for x in range(N + 1)]
visited = [False for x in range(N + 1)]
result = [None for x in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

queue = deque()

queue.append(1)
visited[1] = True

while queue:
    visit = queue.pop()
    for i in tree[visit]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            result[i] = visit

for i in range(2, N+1):
    print(result[i])
