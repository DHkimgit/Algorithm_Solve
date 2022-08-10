def solution(n, lost, reserve):
    answer = n - len(lost)
    for i in range(len(lost)):
        if lost[i] in reserve:
            answer += 1
            reserve.remove(lost[i])
        elif lost[i] + 1 in reserve and lost[i] - 1 in reserve:
            answer += 1
            reserve.remove(lost[i] - 1)
        elif lost[i] + 1 in reserve:
            answer += 1
            reserve.remove(lost[i] + 1)
        elif lost[i] - 1 in reserve:
            answer += 1
            reserve.remove(lost[i] - 1)
        else:
            continue
    return answer

print(solution(9, [2, 3, 7], [1, 3, 4]))