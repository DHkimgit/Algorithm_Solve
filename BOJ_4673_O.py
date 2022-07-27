def d(n):
    result = 0
    if len(str(n)) == 2:
        result = n + (n//10) + (n%10)
    elif len(str(n)) >= 3:
        result += n
        for i in range(len(str(n)) ):
            result += (n % (10 ** (i+1))) // (10 ** i)
            n -= n % (10 ** (i+1))
    else:
        result = 2 * n

    return result

result = []

for i in list(range(1,10001)):
    result.append(d(i))
    if i not in result:
        print(i)
