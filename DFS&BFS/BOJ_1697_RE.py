from collections import deque

N, K = map(int, input().split())

graph = [0 for x in range(200001)]
graph[N] = 1
dx = [1, -1, 2]

queue = deque()
queue.append(N)

flag = 0

while queue:
    current_point = queue.popleft()

    for i in range(3):
        if dx[i] == 2:
            new_point = current_point * 2
        else:
            new_point = current_point + dx[i]

        if new_point == K:
            flag = 1
            graph[new_point] = graph[current_point] + 1
            break
        if new_point >= 200001 or new_point < 0:
            continue
        if graph[new_point] >= 1:
            continue
        else:
            queue.append(new_point)
            graph[new_point] = graph[current_point] + 1

    if flag == 1:
        break

if N == K:
    print(0)
else:
    print(graph[K] -1)
