from collections import deque

N, K = map(int, input().split())

graph = [0 for x in range(200001)]
graph[N] = 1
dx = [1, -1, 2]

queue = deque()
queue.append(N)
flag = 0
while queue:
    x = queue.popleft()
    for i in range(3):
        if dx[i] == 2:
            nx = x * 2
            if nx == K:
                graph[nx] = graph[x] + 1
                flag = 1
                break
            if nx < 0 or nx >= 200000:
                continue
            if graph[nx] >= 1:
                continue
            else:
                queue.append(nx)
                graph[nx] = graph[x] + 1

        else:
            nx = x + dx[i]
            if nx == K:
                graph[nx] = graph[x] + 1
                flag = 1
                break
            if nx < 0 or nx >= 200000:
                continue
            if graph[nx] >= 1:
                continue
            else:
                queue.append(nx)
                graph[nx] = graph[x] + 1

    if flag == 1:
        break
if N == K:
    print(0)
else:   
    print(graph[K] - 1)
