import heapq

V, E = map(int, input().split())
K = int(input())

# 인접 리스트 생성
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 다익스트라 알고리즘 실행
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