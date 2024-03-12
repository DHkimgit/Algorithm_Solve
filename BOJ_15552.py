import sys

T = int(sys.stdin.readline().rstrip())

result = []

for i in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    result.append(a + b)

for i in result:
    print(i)
