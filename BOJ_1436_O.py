N = int(input())

result = []
i = 1

def check_666(s: int):
    word = str(s)
    return '666' in word

while True:
    if check_666(i) == True:
        result.append(i)
    if len(result) == N:
        break
    i += 1

print(result[-1])