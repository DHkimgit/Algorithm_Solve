import copy
N = int(input())
people = []
winrate = []
for i in range(N):
    x, y = map(int, input().split())
    people.append((x, y))

for i in range(N):
    win = 0
    for j in range(N):
        if i == j:
            continue
        if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            win+=1
    winrate.append(win)

result = copy.deepcopy(winrate)
rank = 1
while True:
    tmp = 0
    max_r = max(winrate)
    if max_r == -1:
        break
    for i in range(len(winrate)):
        if winrate[i] == max_r:
            result[i] = rank
            winrate[i] = -1
            tmp += 1
    rank += tmp

for i in range(N):
    if i == N-1:
        print(result[i])
    else:
        print(result[i], end=' ')
