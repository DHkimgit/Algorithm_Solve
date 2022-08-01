def solution(n):
    answer = 0
    tmp = []
    m = str(n)
    for i in range(len(m)):
        tmp.append(m[i])
    tmp.sort(reverse=True)
    answer = "".join(tmp)
    return int(answer)