s = str(input())
t = str(input())

list_str = list(t)

for i in range(len(t) - len(s)):
    if list_str[-1] == 'A':
        list_str.pop()
    else:
        list_str.pop()
        list_str.reverse()

if s == ''.join(list_str):
    print(1)
else:
    print(0)

# 문자열 뒤에 A를 추가
# 문자열 뒤집고 뒤에 B를 추가

# 문자열 뒤에 있는 B를 제거 하고 뒤집기
# 문자열 뒤에 있는 A를 제거