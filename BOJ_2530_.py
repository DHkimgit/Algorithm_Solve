A, B, C = map(int, input().split())

D = int(input())

def calc(sec, A, B, C):
    miniute = sec // 60
    second = sec - 60 * miniute
    if miniute >= 60:
        clock = miniute // 60
        miniute = miniute - clock * 60
    else:
        clock = 0
    
    A += clock
    B += miniute
    C += second

    if C >= 60:
        B += 1
        C -= 60
        if B >= 60:
            A += 1
            B -= 60
    
    elif C < 60 and B >= 60:
        A += 1
        B -= 60
    
    if A >= 24:
        A = A % 24

    return A, B, C

a, b, c = calc(D, A, B, C)
print(a, end=' ')
print(b, end=' ')
print(c)
