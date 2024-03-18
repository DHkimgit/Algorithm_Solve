word = str(input())
word_s = word.lower()
table = [0 for x in range(26)]

for i in range(len(word_s)):
    table[ord(word_s[i]) - 97] += 1
m = max(table)
answer = [index for index, val in enumerate(table) if val == m]
if len(answer) > 1:
    print("?")
else:
    print(chr(answer[0] + 97).upper())
