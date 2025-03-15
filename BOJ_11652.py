import sys
input = sys.stdin.readline
table = dict()

N = int(input())

for i in range(N):
    num = int(input())
    if num in table:
        table[num] += 1
    else:
        table[num] = 1

result = sorted(table.items(), key = lambda item: (-item[1], item[0]))[0][0]

print(result)