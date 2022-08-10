import math
def solution(n):
    tmp = math.sqrt(n)
    if tmp % 1 == 0:
        return (tmp + 1) ** 2
    else:
        return -1