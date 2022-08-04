def solution(a, b):
    answer = ''
    date = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    month = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]
    answer = date[(sum(month[:a-1]) + b) % 7]
    return answer