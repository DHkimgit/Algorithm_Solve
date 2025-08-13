from itertools import combinations
import sys
input = sys.stdin.readline

chicken = []
house = []
N, M = map(int, input().split())
for i in range(N):
    val = list(map(int, input().split()))
    for j in range(N):
        if val[j] == 1:
            house.append((i, j))
        elif val[j] == 2:
            chicken.append((i, j))

candidates = list(combinations(chicken, M))

def get_chicken_distance(chicken_store_list: list):
    result = 0
    for hx, hy in house:
        house_result = 9999999
        for cx, cy in chicken_store_list:
            house_result = min(house_result, calc_distance(hx, hy, cx, cy))
        result += house_result
    return result

def calc_distance(x, y, dx, dy):
    return abs(dx - x) + abs(dy - y)

answer = 9999999
for candidate in candidates:
    answer = min(answer, get_chicken_distance(candidate))
print(answer)

# 백트래킹 -> 시간 초과
# import sys
# input = sys.stdin.readline

# graph = []
# N, M = map(int, input().split())
# for _ in range(N):
#     graph.append(list(map(int, input().split())))

# answer = 9999999

# def get_chicken_distance():
#     house = []
#     chicken = []
#     distance = 0

#     for i in range(N):
#         for j in range(N):
#             if graph[i][j] == 1:
#                 house.append((i, j))
#             if graph[i][j] == 2:
#                 chicken.append((i, j))
    
#     for i in range(len(house)):
#         x, y = house[i]
#         cuurent_house_distance = 9999999
#         for j in range(len(chicken)):
#             cx, cy = chicken[j]
#             cuurent_house_distance = min(cuurent_house_distance, calc_distance(x, y, cx, cy))
#         distance += cuurent_house_distance
#     global answer
#     answer = min(answer, distance)

# def calc_distance(x, y, dx, dy):
#     return abs(dx - x) + abs(dy - y)

# def count_chicken_store():
#     result = 0
#     for i in range(N):
#             for j in range(N):
#                 if graph[i][j] == 2:
#                     result += 1
#     return result

# def backtracking(chicken_store_count: int):
#     if chicken_store_count == M:
#         get_chicken_distance()
#     else:
#         for i in range(N):
#             for j in range(N):
#                 if chicken_store_count > M:
#                     if graph[i][j] == 2:
#                         graph[i][j] = 0
#                         backtracking(chicken_store_count - 1)
#                         graph[i][j] = 2

# backtracking(count_chicken_store())
# print(answer)
