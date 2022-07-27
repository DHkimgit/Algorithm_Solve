N = int(input())
array = [[] for _ in range(N)]

for i in range(N):
    tmp = list(str(input()))
    for j in range(len(tmp)):
        if tmp[j] == '(':
            array[i].append(1)
        else:
            array[i].append(-1)

def array_sum(array):
    result = 0
    for i in range(len(array)):
        result += array[i]
        if result < 0:
            break
    return result

for i in range(N):
    if array_sum(array[i]) == 0:
        print('YES')
    else:
        print('NO')
