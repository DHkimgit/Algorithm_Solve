import math
n = 1003002
array = [True for i in range(n + 1)]
k = []
x = int(input())

def Palindrome(x):
    k = str(x)
    lenth = len(k)
    
    if  lenth == 2:
        if k[0] == k[1]:
            return True
        else:
            return False

    elif lenth == 1:
        return True

    elif lenth != 1 and lenth != 2:
        if lenth % 2 != 0:
            for i in range(lenth):
                if lenth - 1 - i != i:
                    if k[lenth-1 - i] == k[i]:
                        continue 
                    else:
                        return False
                elif lenth - 1 - i == i:
                    return True
        
        elif lenth % 2 == 0:
            for i in range(lenth):
                if lenth - 1 - 2*i != 1:
                    if k[lenth-1 - i] == k[i]:
                        continue 
                    else:
                        return False
                elif lenth - 1 - 2*i == 1:
                    if k[lenth-1 - i] == k[i]:
                        return True
                    return False

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1

for i in range(x, n):
    if array[i] == True and Palindrome(i) == True:
        continue
    else:
        array[i] = False

for i in range(2, n):
    if i >= x and array[i]:
        print(i)
        break
