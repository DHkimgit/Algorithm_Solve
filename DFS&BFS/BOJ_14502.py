from collections import deque
import sys
import copy
input = sys.stdin.readline

lab = []
N, M = map(int, input().split())
for _ in range(N):
    lab.append(list(map(int, input().split())))

def bfs_result():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    tmp_lab = copy.deepcopy(lab)
    queue = deque()

    for i in range(N):
        for j in range(M):
            if tmp_lab[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if tmp_lab[nx][ny] == 0:
                tmp_lab[nx][ny] = 2
                queue.append((nx, ny))
    
    global result
    current_result = 0

    for i in range(N):
        current_result += tmp_lab[i].count(0)
    
    result = max(result, current_result)

def wall_backtracking(wall_count: int):
    if wall_count == 3:
        bfs_result()
        return
    
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall_backtracking(wall_count + 1)
                lab[i][j] = 0

result = 0
wall_backtracking(0)
print(result)
