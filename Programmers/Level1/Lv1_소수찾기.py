import math
array = [True for i in range(1, 1000000)]
def solution(n):
    result = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i*j] = False
                j +=1
    for i in range(2, n+1):
        if array[i]:
            result +=1
    return result