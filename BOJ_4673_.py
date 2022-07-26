def d(n):
    result = 0
    for i in range(len(str(n))):
        result += n // (10**i)
    return result
print(d(39))