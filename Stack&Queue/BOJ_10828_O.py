N = int(input())
order = []
stack = []

for i in range(N):
    tmp = input()
    order.append(tmp)

for i in range(len(order)):
    if order[i].split()[0] == 'push':
        stack.append(order[i].split()[1])

    elif order[i] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    
    elif order[i] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    
    elif order[i] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    
    elif order[i] == 'size':
        print(len(stack))
