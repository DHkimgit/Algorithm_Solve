N, M = map(int,input().split())

data = [[[[] for col in range(8)] for row in range(8)] for depth in range(8)]

for i in range(N):
    tmp = list(input().split())
    first = ord(str(tmp[2])) - 65
    second = ord(str(tmp[3])) - 65
    third = ord(str(tmp[4])) - 65
    data[first][second][third].append(tmp[1])

result = []

for j in range(M):
    st1, st2, st3 = map(str, input().split())
    first = ord(st1) - 65
    second = ord(st2) - 65
    third = ord(st3) - 65
    if len(data[first][second][third]) == 1:
        result.append(data[first][second][third][0])
    elif len(data[first][second][third]) >=2:
        result.append('?')
    else:
        result.append('!')

for i in result:
    print(i)
