from collections import deque

T = int(input())

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def BFS():
    length = int(input())
    cur_x, cur_y = map(int, input().split())
    tar_x, tar_y = map(int, input().split())

    if cur_x == tar_x and cur_y == tar_y:
        print(0)
        return
    
    visited = [[0 for _ in range(length)] for _ in range(length)]

    queue = deque()
    queue.append([cur_x, cur_y])
    flag = 0

    while True:
        current_point = queue.popleft()

        cur_x = current_point[0]
        cur_y = current_point[1]

        for i in range(8):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if next_x == tar_x and next_y == tar_y:
                print(visited[cur_x][cur_y] + 1)
                flag = 1
                break

            if next_x < 0 or next_x >= length or next_y < 0 or next_y >= length:
                continue
            if visited[next_x][next_y] != 0:
                continue
            else:
                visited[next_x][next_y] = visited[cur_x][cur_y] + 1
                queue.append([next_x, next_y])

        if flag == 1:
            break

for i in range(T):
    BFS()

