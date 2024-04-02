sticks = str(input())

stack = []
result = 0
height = 0
for i in range(len(sticks)):
    if sticks[i] == '(':
        stack.append(sticks[i])
        height += 1
    elif sticks[i] == ')':
        if stack[-1] == '(':
            stack.pop()
            height -= 1
            result += height
        else:
            result += 1
            height -= 1

        stack.append(')')

print(result)