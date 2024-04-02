from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
li = deque([i + 1 for i in range(n)])

result = []
while li:
    for i in range(k - 1):
        li.append(li.popleft())

    result.append(li.popleft())
print('<', end='')
for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i], end='')
    else:
        print(result[i], end=', ')
print('>')
# print('<' + ', '.join(str(o) for o in result)+'>')