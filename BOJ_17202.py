def combine(a, b):
    result = []
    k = len(a)
    for i in range(k):
        result.append(a[i])
        result.append(b[i])
    return ''.join(result)
A = str(input())
B = str(input())
first = combine(A, B)

def play(number):
    result = []
    k = len(number)
    for i in range(k - 1):
        T = int(int(number[i]) + int(number[i + 1])) % 10
        result.append(str(T))
    inputs = ''.join(result)
    if len(inputs) == 2:
        print(inputs)
        return 0
        
    else:
        play(inputs)

dwq = play(first)
