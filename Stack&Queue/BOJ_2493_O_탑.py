N = int(input())
top = list(map(int, input().split()))

stack = []
result = []

for i in range(N):
    if len(stack) == 0:
        stack.append((i + 1, top[i]))
        result.append(0)
    else:
        while(len(stack) > 0):
            if stack[-1][1] > top[i]:
                result.append(stack[-1][0])
                break
            else:
                stack.pop()
    
    if len(stack) == 0:
        result.append(0)
    
    stack.append([i + 1, top[i]])

print(' '.join(str(i) for i in result))

