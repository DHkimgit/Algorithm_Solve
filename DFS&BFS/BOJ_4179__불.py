from collections import deque
import copy

R, C = map(int, input().split())

maps = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(R):
    maps.append(list(map(str, input())))

# 지훈이가 서있는 위치, 불들의 위치 구하기
j_init = []
fires = []

for i in range(R):
    for j in range(C):
        if maps[i][j] == 'J':
            j_init = [i, j]
        if maps[i][j] == 'F':
            fires.append((i, j))

# 불을 탈출점까지 도달시키기
fire_vis = [[0]*C for _ in range(R)]
fire_maps = copy.deepcopy(maps)

fire_maps[j_init[0]][j_init[1]] = '.'

queue_fire = deque()

for i in range(len(fires)):
    queue_fire.append(fires[i])
    fire_vis[fires[i][0]][fires[i][1]] = 1
    fire_maps[fires[i][0]][fires[i][1]] = 0

while queue_fire:
    x, y = queue_fire.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            continue
        
        if fire_maps[nx][ny] == '#' or fire_vis[nx][ny] == 1:
            continue
        
        else:
            queue_fire.append((nx, ny))
            fire_vis[nx][ny] = 1
            fire_maps[nx][ny] = fire_maps[x][y] + 1

jh_vis = [[0]*C for _ in range(R)]
jh_vis[j_init[0]][j_init[1]] = 1

jh_maps = copy.deepcopy(maps)
jh_maps[j_init[0]][j_init[1]] = 0

queue_jh = deque()

queue_jh.append((j_init[0], j_init[1]))

ex_x = -1
ex_y = -1

while queue_jh:
    x, y = queue_jh.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            ex_x = x
            ex_y = y
            break
        
        if jh_maps[nx][ny] == '#' or jh_maps[nx][ny] == 'J' or jh_vis[nx][ny] == 1:
            continue

        if isinstance(fire_maps[nx][ny], int) and jh_maps[x][y] + 1 >= fire_maps[nx][ny]:
            continue
        
        else:
            queue_jh.append((nx, ny))
            jh_vis[nx][ny] = 1
            jh_maps[nx][ny] = jh_maps[x][y] + 1

min_t = 99999999

if ex_x==-1 and ex_y==-1:
    print("IMPOSSIBLE")
else:
    for i in range(C):
        if isinstance(jh_maps[0][i], int) and jh_maps[0][i] <= min_t:
            min_t = jh_maps[0][i]
    for i in range(C):
        if isinstance(jh_maps[R-1][i], int) and jh_maps[R-1][i] <= min_t:
            min_t = jh_maps[R-1][i]
    for i in range(R):
        if isinstance(jh_maps[i][0], int) and jh_maps[i][0] <= min_t:
            min_t = jh_maps[i][0]
    for i in range(R):
        if isinstance(jh_maps[i][C-1], int) and jh_maps[i][C-1] <= min_t:
            min_t = jh_maps[i][C-1]
    
    print(min_t + 1)




# print(fire_maps)
# print(jh_maps)