n = int(input())
result = [['k' for x in range(n)] for x in range(n)]

def modf(x, y):
    result[y][x + 1] = '*'
    result[y + 1][x] = '*'
    result[y + 1][x + 1] = '*'
    result[y][x - 1] = '*'
    result[y - 1][x] = '*'
    result[y - 1][x - 1] = '*'
    result[y - 1][x + 1] = '*'
    result[y + 1][x - 1] = '*'

def find_center(x, y, N):

    nexts = N//3

    if nexts == 1:
        modf(x, y)
        return
    find_center(x, y + nexts, nexts)
    find_center(x + nexts, y, nexts)
    find_center(x + nexts, y + nexts, nexts)
    find_center(x, y - nexts, nexts)
    find_center(x - nexts, y, nexts)
    find_center(x - nexts, y - nexts, nexts)
    find_center(x - nexts, y + nexts, nexts)
    find_center(x + nexts, y - nexts, nexts)

find_center(n // 2, n // 2, n)

for i in range(len(result)):
    for j in range(len(result[i])):
        if result[i][j] == 'k':
            result[i][j] = ' '

for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end='')
    print('')