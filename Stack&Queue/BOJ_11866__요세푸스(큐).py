N, K = map(int, input().split())

queues = [x for x in range(1, N+1)]
index = 1
pointer = 0
result = []

while queues:
    if pointer >= len(queues):
        pointer = 0

    if index % K == 0:
        result.append(queues.pop(pointer))
        index += 1
        
    else:
        index += 1
        pointer += 1

print("<", end='')
for i in range(N):
    if i != N-1:
        print(result[i], end=', ')
    else:
        print(result[i], end='')
print(">")

# 큐를 이용한 풀이
from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
li = deque([i + 1 for i in range(n)])
print(li)
order = []
while li:
    for i in range(k - 1):
        li.append(li.popleft())
        print(li)
    order.append(li.popleft())
print('<' + ', '.join(str(o) for o in order)+'>')
