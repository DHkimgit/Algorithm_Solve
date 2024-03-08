input_str = list(input())
result = [0]*26

for i in range(len(input_str)):
    index = ord(input_str[i]) - 97
    result[index] += 1

for j in range(len(result)):
    print(result[j], end=' ')