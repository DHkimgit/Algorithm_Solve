import sys
lists = []
N = int(input())
for _ in range(N):
    lists.append(int(sys.stdin.readline().rstrip()))

lists.sort()

for i in range(N):
    print(lists[i])