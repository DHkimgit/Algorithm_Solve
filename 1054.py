import re
from itertools import product
from itertools import permutations
N = int(input())

strs = []

for i in range(N):
    value = input()
    strs.append(value)

def isPalindrome(s: str):
    s = s.lower()

    s = re.sub('[^a-z0-9]', '', s)

    return s == s [::-1]

result = 0
repeat_value = 1

while True:
    if repeat_value == N+1:
        break
    permutation_with_repetitions = [''.join(i) for i in list(permutations(strs, repeat_value)) if isPalindrome(''.join(i)) == True]
    result += len(permutation_with_repetitions)
    repeat_value += 1

print(result)
