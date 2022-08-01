def solution(answers):
    answer = []
    tmp = []
    student_1 = [1, 2, 3, 4, 5] * 2000
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    student_1_score = 0
    student_2_score = 0
    student_3_score = 0
    
    for i in range(len(answers)):
        if answers[i] == student_1[i]:
            student_1_score += 1
        if answers[i] == student_2[i]:
            student_2_score += 1
        if answers[i] == student_3[i]:
            student_3_score += 1
    
    if student_1_score > student_2_score and student_1_score > student_3_score:
        answer.append(1)
    elif student_2_score > student_1_score and student_2_score > student_3_score:
        answer.append(2)
    elif student_3_score > student_1_score and student_3_score > student_2_score:
        answer.append(3)
    elif student_1_score == student_2_score and student_1_score > student_3_score:
        answer.append(1)
        answer.append(2)
    elif student_1_score == student_3_score and student_1_score > student_2_score:
        answer.append(1)
        answer.append(3)
    elif student_2_score == student_3_score and student_2_score > student_1_score:
        answer.append(2)
        answer.append(3)
    elif student_2_score == student_3_score and student_2_score == student_1_score:
        answer.append(1)
        answer.append(2)
        answer.append(3)
        
    return answer