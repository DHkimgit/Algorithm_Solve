from collections import deque
N = int(input())
d = deque([])
order = []

for _ in range(N):
    order.append(input())

def play(order):
    if order == 'front':
        if len(list(d)) != 0:
            print(d[0])
        else:
            print(-1)
    
    elif order == 'back':
        if len(list(d)) != 0:
            print(d[-1])
        else:
            print(-1)
    
    elif order == 'size':
        print(len(list(d)))

    elif order == 'empty':
        if len(list(d)) != 0:
            print(0)
        else:
            print(1)
    
    elif order == 'pop':
        if len(list(d)) != 0:
            print(d.popleft())
        else:
            print(-1)

    else:
        if order[0:4] == 'push':
            d.append(order[5:])

for i in range(N):
    play(order[i])
    