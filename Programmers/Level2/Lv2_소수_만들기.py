from itertools import combinations

def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        target = sum(i)
        for j in range(2, target):
            if target%j == 0:
                break
        else:
            answer +=1
    return answer
