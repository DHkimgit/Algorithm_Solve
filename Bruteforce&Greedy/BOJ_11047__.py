import sys
input = sys.stdin.readline
N, K = map(int, input().split())

coins = []

for i in range(N):
    coins.append(int(input()))

coins.reverse()
count = 0

while(K > 0):
    for i in range(N):
        if K - coins[i] >= 0:
            count += K//coins[i]
            K = K % coins[i]

print(count)
