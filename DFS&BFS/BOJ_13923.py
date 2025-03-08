from collections import deque

N, K = map(int, input().split())

graph = [[0, -1] for _ in range(100001)]
graph[N][0] = 1

dx = [1, -1, 2]

queue = deque()
queue.append(N)

while queue:
    current_point = queue.popleft()
    if current_point == K:
        print(graph[K][0] - 1)
        break

    for i in range(3):
        if dx[i] == 2:
            next_point = current_point * 2
        else:
            next_point = current_point + dx[i]

        if 0 <= next_point < 100001 and graph[next_point][0] == 0:
            graph[next_point][0] = graph[current_point][0] + 1
            graph[next_point][1] = current_point
            queue.append(next_point)

result = [K]

while True:
    if graph[K][1] == -1:
        break
    result.append(graph[K][1])
    K = graph[K][1]

print(*result[::-1])

# while True:
#     x = graph[K]


# if N != K:
#     print(len(graph[K]) - 1)
#     for i in graph[K]:
#         print(i, end=" ")
# from collections import deque

# N, K = map(int, input().split())

# graph = [[] for x in range(200001)]
# graph[N].append(N)

# dx = [1, -1, 2]
# flag = 0

# queue = deque()

# queue.append(N)

# if N == K:
#     print(0)
#     print(N)

# while queue:
#     current_point = queue.popleft()

#     for i in range(3):
#         if dx[i] == 2:
#             next_point = current_point * 2
#         else:
#             next_point = current_point + dx[i]
        
#         if next_point == K:
#             for x in graph[current_point]:
#                 graph[next_point].append(x)
#             graph[next_point].append(next_point)
#             flag = 1
#             break
#         if next_point < 0 or next_point >= 200001:
#             continue

#         if graph[next_point]:
#             continue
#         else:
#             queue.append(next_point)
#             for x in graph[current_point]:
#                 graph[next_point].append(x)
#             graph[next_point].append(next_point)

#     if flag == 1:
#         break

# if N != K:
#     print(len(graph[K]) - 1)
#     for i in graph[K]:
#         print(i, end=" ")
