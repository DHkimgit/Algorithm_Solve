import sys
N = int(input())

meeting = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    meeting.append((a, b))

meeting.sort(key = lambda x : (x[1], x[0]))

current_time = 0

result = 0

for i in range(N):
    if meeting[i][0] >= current_time:
        result += 1
        current_time = meeting[i][1]

print(result)
