N = int(input())
cards = list(map(int, input().split()))

M = int(input())
cases = list(map(int, input().split()))

table = [0 for x in range(10000001)]
table_m = [0 for x in range(10000001)]

for i in range(N):
    if cards[i] >= 0:
        table[cards[i]] += 1
    else:
        table_m[-cards[i]] += 1

for i in range(M):
    if cases[i] >= 0:
        print(table[cases[i]], end=' ')
    else:
        print(table_m[-cases[i]], end=' ')