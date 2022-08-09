def solution(d, budget):
    d.sort()
    temp = 0
    answer = 0
    for i in range(len(d)):
        temp += d[i]
        if temp > budget:
            break
        answer += 1
        if temp >= budget:
            break
        
    return answer