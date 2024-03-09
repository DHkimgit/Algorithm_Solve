N = int(input())

result = []

def DigitSum(x):
    result = 0
    for i in str(x):
        result += int(i)
    return result

for i in range(1, N+1):

    target = DigitSum(i) + i

    if target == N:
        result.append(i)
        break

if result:
    print(result[0])

else:
    print(0)
