N, r, c = map(int, input().split())
result = 0

while N != 0:
    N -= 1
    length = 2 ** N

    # 2사분면
    if r < length and c < length:
        result += 0

    # 1사분면
    elif r < length and c >= length: 
        result += length * length
        c -= length
        
    # 3사분면    
    elif r >= length and c < length: 
        result += length  * length * 2
        r -= length 

    # 4사분면    
    else:
        result += length * length * 3
        r -= length
        c -= length

print(result)