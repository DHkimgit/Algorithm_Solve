from itertools import product
import re

N = int(input())
L = int(input())
strs = []

for i in range(N):
    value = input()
    strs.append(value)

def findMaxMin(str):
    MAX = 0
    MIN = len(str[0])
    for i in range(len(str)):
        if len(str[i]) > MAX:
            MAX = len(str[i])
        if len(str[i]) < MIN:
            MIN = len(str[i])
    
    return MAX, MIN

MAX, MIN = findMaxMin(strs)

def isPalindrome(s: str):
    s = s.lower()

    s = re.sub('[^a-z0-9]', '', s)

    return s == s [::-1]

repeat_value = 1
result = 0

remit = L // MIN 

while True:
    if repeat_value == remit + 1:
        break
    permutation_with_repetitions = [''.join(i) for i in list(product(strs, repeat=repeat_value)) if len(''.join(i)) == L and isPalindrome(''.join(i)) == True]
    print(permutation_with_repetitions)
    if permutation_with_repetitions == []:
        pass
    else:
        for i in range(len(permutation_with_repetitions)):
            if isPalindrome(permutation_with_repetitions[i]) == True:
                result += 1
            else:
                pass
    
    repeat_value += 1

print(result)

# [''.join(i) for i in list(product(['A', 'C', 'G', 'T'], repeat=4))]
# test = [''.join(i) for i in list(product(['AK', 'AA', 'BB', 'BCC', 'CBBB'], repeat=2))]
# test_updated = [value for value in test if len(value) == 4]

# # 단어의 길이 L, 주어진 단어 중 가장 짧은 단어의 길이 MIN, 가장 긴 단어의 길이 MAX
# # L 이 5고 MIN 이 2이면 repeat 1 부터 들어가야 함 [DD, FE, KFE, GFD, FEDS], DDKFE 
# print(test)
# print(test_updated)

# def isPalindrome(s: str) -> bool:
#     strs: Deque = deque()
#     for char in s:
#         strs.append(char)

#     while len(strs) > 1:
#         if strs.popleft() != strs.pop():
#             return False
#     return True