result = [] 
while True:
    k = 0
    s = str(input())
    if s == '#':
        break
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'A':
            k += 1
        elif s[i] == 'e' or s[i] == 'E':
            k += 1
        elif s[i] == 'i' or s[i] == 'I':
            k += 1
        elif s[i] == 'o' or s[i] == 'O':
            k += 1
        elif s[i] == 'u' or s[i] == 'U':
            k += 1
    result.append(k)

for i in result:
    print(i)