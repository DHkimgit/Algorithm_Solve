A, B, C = map(int, input().split())

def solution(A, B, C):
    if B == 0:
        return 1
    elif B == 1:
        return A % C 
    
    result = solution(A, B//2, C)
    result = result * result % C 

    if B % 2 == 0:
        return result
    else:
        return (result * A) % C

print(solution(A, B, C))