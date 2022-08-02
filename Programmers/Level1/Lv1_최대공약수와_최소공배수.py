def solution(n, m):
    answer = []
    answer.append(GCD(n, m))
    answer.append(LCM(n, m))
    return answer

def GCD(n, m):
    while(m):
        n, m = m, n%m
    return n

def LCM(n, m):
    result = (n * m)//GCD(n, m)
    return result
