import math
def solution(s):
    answer = ''
    lenth = len(s)
    if len(s) % 2 == 0:
        answer = s[lenth//2 - 1] + s[lenth//2]
    else:
        answer = s[lenth//2]
    return answer