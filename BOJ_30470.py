import sys
input = sys.stdin.readline

N = int(input())

current_max = 0
stack = []

for i in range(N):
    a, b = map(int, input().split())
    if a == 1:
        if b > current_max:
            current_max = b
        stack.append(b)
    else:
        monster_length = max(current_max - b, 0)
        tmp = 0
        while stack:
            if stack[-1] > monster_length:
                stack.pop()
                tmp += 1
            else:
                break
        for i in range(tmp):
            stack.append(monster_length)
        current_max = monster_length

result = 0
for val in stack:
    result += val

print(result)
