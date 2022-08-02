def solution(seoul):
    index = 0
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            index = i
    answer = "김서방은 {}에 있다".format(index)
    return answer