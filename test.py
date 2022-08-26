array = [101, 102, 103, 104, 202, 204, 303]
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


print(Palindrome(2))