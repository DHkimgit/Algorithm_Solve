from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

dx = [1, -1]
dy = [1, 1]

mountain = [['O' for y in range(2*N + 1)] for x in range(N+1)]
visited = [[0 for y in range(2*N + 1)] for x in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    mountain[b][a] = 'X'

queue = deque()

queue.append((0, 0))
visited[0][0] = 1
max_height = 0

while queue:
    x, y = queue.popleft()

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= N+1 or ny >= 2*N+1 or nx < 0 or ny < 0:
            continue
        
        if ny <= nx - 1 or ny >= 2*N - nx + 1:
            continue

        if mountain[nx][ny] == 'X':
            continue
        
        if visited[nx][ny] == 1:
            continue
        
        queue.append((nx, ny))
        visited[nx][ny] = 1

        if nx > max_height:
            max_height = nx

if visited[0][2*N] != 1:
    print(-1)

else:
    print(max_height)
# ny =< nx - 1 or ny >= 2*N - nx + 1
# N = 4 
# OOOOXOOOO
# XOOOOOOOX
# XXOOOOOXX
# XXXOOOXXX
# XXXXOXXXX

# N = 3
# OOOOOOO
# XOOXOOX
# XXOOOXX
# XXXOXXX

# for i in range(N + 1):
#     for j in range(i):
#         mountain[i].append('X')
#     for k in range(N - i):
#         mountain[i].append('O')
#     mountain[i].append('O')
#     for l in range(N - i):
#         mountain[i].append('O')
#     for m in range(i):
#         mountain[i].append('X')