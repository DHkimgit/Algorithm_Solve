N, M = map(int, input().split())
board_w =[['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
board_b =[['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

input_b = []
result = 9999999999999999

for _ in range(N):
    input_b.append(list(input()))

def check_board(N, M):
    result_w = 0
    result_b = 0
    for i in range(8):
        for j in range(8):
            if board_w[i][j] == input_b[N+i][M+j]:
                result_w += 1
            if board_b[i][j] == input_b[N+i][M+j]:
                result_b += 1
    return min(result_b, result_w)

for i in range(N-7):
    for j in range(M-7):
        result=min(result, check_board(i, j))

print(result)
