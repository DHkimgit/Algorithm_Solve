def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    completion.append('tmp')
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
