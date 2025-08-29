# 이름: 김두현
# 학번: 2021136017
# 날짜: 2025-05-11

import heapq
import sys
input = sys.stdin.readline 
INF = float('inf')

def extract_min(priority_queue):
    return heapq.heappop(priority_queue)

def dijkstra(graph, root_node, vertex_num):
    distances = [INF] * (vertex_num + 1)
    distances[root_node] = 0

    priority_queue = []
    heapq.heappush(priority_queue, (0, root_node))

    while priority_queue:
        current_distance, current_node = extract_min(priority_queue)

        if current_distance > distances[current_node]:
            continue

        if current_node in graph:
            for neighbor_node, weight in graph[current_node]:
                update_distance = current_distance + weight
                if update_distance < distances[neighbor_node]:
                    distances[neighbor_node] = update_distance
                    heapq.heappush(priority_queue, (update_distance, neighbor_node))
    
    return distances

n, m = map(int, input().split())
graph = {} 

for _ in range(m):
    u, v, w = map(int, input().split())
    if u not in graph:
        graph[u] = []
    graph[u].append((v, w))

start = int(input())

result = dijkstra(graph, start, n)

for i in range(1, n + 1):
    if result[i] == INF:
        print("INF")
    else:
        print(result[i])
