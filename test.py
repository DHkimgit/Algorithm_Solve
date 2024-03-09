def DigitSum(x):
    result = 0
    for i in str(x):
        result += int(i)
    return result

print(DigitSum(345))