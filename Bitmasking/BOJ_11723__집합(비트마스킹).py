import sys
input = sys.stdin.readline

bit = 0b0

M = int(input())

for i in range(M):
    order = input().split()

    if order[0] == 'add':
        bit |= (0b1 << int(order[1]))
    elif order[0] == 'remove':
        bit &= ~(0b1 << int(order[1]))
    elif order[0] == 'check':
        print(0b1 if bit & (0b1 << int(order[1])) != 0 else 0)
    elif order[0] == 'toggle':
        bit ^= (0b1 << int(order[1]))
    elif order[0] == 'empty':
        bit = 0b0
    elif order[0] == 'all':
        bit = 0b111111111111111111111
    

