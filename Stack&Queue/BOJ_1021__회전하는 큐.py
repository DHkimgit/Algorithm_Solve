from collections import deque

N, M = map(int, input().split())
target = list(map(int, input().split()))

queue = deque(range(1, N + 1))

result = 0

for i in target:
    while True:
        if i == queue[0]:
            queue.popleft()
            break

        else:
            if queue.index(i) <= len(queue) // 2:
                queue.rotate(-1)
                result += 1

            else:
                queue.rotate(1)
                result += 1

print(result)            