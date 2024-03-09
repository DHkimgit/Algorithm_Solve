result = []

while True:
    inp = str(input())
    if inp == '0':
        break
    if inp == inp[::-1]:
        result.append('yes')
    else:
        result.append('no')

for i in range(len(result)):
    print(result[i])