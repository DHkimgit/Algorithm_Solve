import re
# input_str = input()

# strs: Deque = collections.deque()

# for char in input_str:
#     if char.isalnum():
#         strs.append(char.lower())

# while len(strs) > 1:
#     if strs.popleft() != strs.pop():
#         print(0)
#         exit(0)

def isPalindrome(s: str):
    s = s.lower()

    s = re.sub('[^a-z0-9]', '', s)

    return s == s [::-1]

t = isPalindrome('assad')

print(t)