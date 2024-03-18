from collections import deque

computer = int(input())
edge = int(input())
graph = [[] for x in range(computer + 1)]
visited = [False] * (computer+1)
result = 0

for i in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)
visited[1] = True

while queue:
    t = queue.popleft()

    for i in graph[t]:
        if visited[i] == False:
            queue.append(i)
            visited[i] = True

for i in visited:
    if i:
        result += 1

print(result - 1)
