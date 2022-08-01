def solution(n):
    tmp = []
    m = str(n)
    for i in range(len(m) - 1, -1, -1):
        tmp.append(int(m[i]))
    return tmp
