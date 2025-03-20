K = int(input())
S = input()

current_N = 0
current_S = 0
former_N = 0
former_S = 0
former_str = None
result = 0

for char in S:
    if char == 'N' and former_str == None:
        current_N += 1
        former_str = 'N'
    if char == 'S' and former_str == None:
        current_S += 1
        former_str = 'S'
    if char == 'N' and former_str == 'N':
        current_N += 1
        if current_N <= former_S:
            result = max(result, current_N)
        else:
            former_S = 0
        former_str = 'N'
    if char == 'N' and former_str == 'S':
        former_S = current_S
        current_S = 0
        current_N += 1
        if current_N <= former_S:
            result = max(result, current_N)
        else:
            former_S = 0
        former_str = 'N'
    if char == 'S' and former_str == 'S':
        current_S += 1
        if current_S <= former_N:
            result = max(result, current_S)
        else:
            former_N = 0
        former_str = 'S'
    if char == 'S' and former_str == 'N':
        former_N = current_N
        current_N = 0
        current_S += 1
        if current_S <= former_N:
            result = max(result, current_S)
        else:
            former_N = 0
        former_str = 'S'

print(result * 2)
