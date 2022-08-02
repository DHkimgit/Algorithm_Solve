def solution(s, n):
    answer = []
    k = 0
    for i in range(len(s)):
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            k = ord(s[i]) + n
            if 90 <= k <= 115:
                k -= 26
        elif ord(s[i]) >= 97 and ord(s[i]) <= 122:
            k = ord(s[i]) + n
            if k > 122:
                k -= 26
        elif ord(s[i]) == 32:
            k = 32
        answer.append(chr(k))
    result = "".join(answer)
    return result

def caesar(s, n):
    answer = ""
    for i in s:
        if i == " ":
            answer += i
        else:
            temp = ord(i) + n
            if (ord(i) >= 65 and ord(i) <= 90):
                if temp > 90:
                    temp = temp - 26
            if (ord(i) >= 97 and ord(i) <= 122):
                if temp > 122:
                    temp = temp - 26
            answer += chr(temp)
    return answer

print(solution("ZasDwefFvsdsf DWdsdwDFcDswvdfgfD", 13))