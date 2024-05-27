V, E = map(int, input().split())
K = int(input())
graph = [[99 for x in range(V + 1)] for x in range(V + 1)]
result = graph[K]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u][v] = w
visited = []

# 시작 노드 => 처음 방문하는 노드
visited.append(K) # 시작 노드 방문 추가
i = result.index(min(result)) #2

for _ in range(V):
    visited.append(i)
    for j in range(1, len(graph[i])):
        tmp = min(result[j], graph[i][j] + result[i])
        if tmp < result[j]:
            result[j] = tmp

    min_value = float('inf')
    min_index = -1

    for i in range(len(result)):
        if i not in visited and result[i] < min_value:
            min_value = result[i]
            min_index = i
    
    i = min_index

result[K] = 0

for i in range(1, V + 1):
    if result[i] != 99:
        print(result[i])
    else:
        print('INF')

#============================================
import heapq

V, E = map(int, input().split())
K = int(input())

# 인접 리스트
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = [float('inf')] * (V + 1)
distance[K] = 0
pq = [(0, K)]  # (거리, 노드) 튜플을 우선순위 큐에 저장

while pq:
    dist, now = heapq.heappop(pq)
    if distance[now] < dist:  # 이미 처리된 노드라면 무시
        continue
    for next_node, weight in graph[now]:
        cost = dist + weight
        if cost < distance[next_node]:
            distance[next_node] = cost
            heapq.heappush(pq, (cost, next_node))

# 결과 출력
for i in range(1, V + 1):
    if distance[i] == float('inf'):
        print('INF')
    else:
        print(distance[i])