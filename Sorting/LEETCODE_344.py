from typing import List

S = list(map(str, input().split()))

def reverseString(s:List[str]) -> None:
    s.reverse()

def reverseStringTwoPointer(s:List[str]) -> None:
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

reverseStringTwoPointer(S)

print(S)
