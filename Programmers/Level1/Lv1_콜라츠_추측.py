def solution(n):
    tmp = 0
    while True:
        if n == 1:
            break
        elif tmp > 500:
            tmp = -1
            break
        elif n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
        tmp += 1
    return tmp