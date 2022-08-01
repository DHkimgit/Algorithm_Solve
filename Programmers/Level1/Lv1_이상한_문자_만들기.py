def solution_timeover(s):
    tmp = s.split()
    result = [[] for _ in range(len(tmp))]
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            if j == 0:
                result[i].append(tmp[i][j].upper())
            elif j%2 != 0:
                result[i].append(tmp[i][j].lower())
            else:
                result[i].append(tmp[i][j].upper())
    results = []
    for k in range(len(result)):
        results.append("".join(result[k]))
    final = " ".join(results)
    return final

def solution_correct(s):
    answer = ''
    new_list = s.split(' ')
    for i in new_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer+= ' '
    return answer[0:-1]

s = input()
print(solution(s))