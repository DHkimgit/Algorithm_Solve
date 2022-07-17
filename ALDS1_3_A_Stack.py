polandList = list(input().split())
polandList.reverse()

numList = []
stack = []

for i in range(len(polandList)):
    tmp = polandList.pop()
    try:
        if (str(type(int(tmp))) == "<class 'int'>"):
            stack.append(int(tmp))
    except ValueError:
        if tmp == '*':
            num1 = stack.pop()
            num2 = stack.pop()
            result = num1 * num2
            stack.append(result)
        elif tmp == '+':
            num1 = stack.pop()
            num2 = stack.pop()
            result = num1 + num2
            stack.append(result)
        elif tmp == '-':
            num1 = stack.pop()
            num2 = stack.pop()
            result = num2 - num1
            stack.append(result)

print(stack[0])
