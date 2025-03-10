visited = [[False for _ in range(5)] for _ in range(5)]

K = int(input())

for _ in range(K):
    x, y = map(int, input().split())
    visited[x-1][y-1] = True

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

total = 25 - K
result = 0

visited[0][0] = True

def dfs(x: int, y: int, cnt: int):
    global result
    if x == 4 and y == 4 and cnt == total:
        result += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                continue
            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            dfs(nx, ny, cnt + 1)
            visited[nx][ny] = False

dfs(0, 0, 1)
print(result)
