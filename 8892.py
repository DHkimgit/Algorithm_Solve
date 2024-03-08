import re
from itertools import permutations

T = int(input())

def isPalindrome(s: str):
    s = s.lower()

    s = re.sub('[^a-z0-9]', '', s)

    return s == s [::-1]

result = []

for i in range(T):
    k = int(input())
    input_str = []

    for i in range(k):
        value = str(input())
        input_str.append(value)
    
    falindromes = [''.join(i) for i in list(permutations(input_str, 2)) if isPalindrome(''.join(i)) == True]
    if falindromes:
        result.append(falindromes[0])
    else:
        result.append(0)

for i in range(len(result)):
    print(result[i])
