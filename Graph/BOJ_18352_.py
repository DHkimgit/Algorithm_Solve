import heapq
import sys
input = sys.stdin.readline 
INF = float('inf')

N, M, K, X = map(int, input().split())

graph = [[] for x in range(N + 1)]

for i in range(M):
    start_node, land_node = map(int, input().split())
    graph[start_node].append(land_node)

def dijkstra(graph : list, vertax_num: int, start_node: int):
    result = [INF] * (vertax_num + 1)
    result[start_node] = 0

    priority_queue = []
    heapq.heappush(priority_queue, (0, start_node))

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > result[current_node]:
            continue

        if graph[current_node]:
            for neighbor_node in graph[current_node]:
                update_distance = current_distance + 1
                if update_distance < result[neighbor_node]:
                    result[neighbor_node] = update_distance
                    heapq.heappush(priority_queue, (update_distance, neighbor_node))
    
    return result

result = dijkstra(graph, N, X)
flag = False
for i in range(N+1):
    if result[i] == K:
        print(i)
        flag = True

if not flag:
    print(-1)