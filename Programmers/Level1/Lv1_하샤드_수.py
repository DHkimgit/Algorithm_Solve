def solution(x):
    result = 0
    m = str(x)
    for i in m:
        result += int(i)
    if x % result == 0:
        return True
    else:
        return False
