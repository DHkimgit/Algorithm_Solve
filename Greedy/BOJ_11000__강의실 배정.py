import sys
import heapq
N = int(input())
lec = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    lec.append((a, b))

lec.sort(key = lambda x : (x[0], x[1]))
room = []
heapq.heappush(room, 0)
for i in range(N):
    k = heapq.heappop(room)
    if lec[i][0] >= k:
        heapq.heappush(room, lec[i][1])

    else:
        heapq.heappush(room, k)
        heapq.heappush(room, lec[i][1])

print(len(room))
