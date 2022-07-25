import sys
input = sys.stdin.readline

N, M = map(int, input().split())

array = [[] for _ in range(M)]

# 최종 결과 출력을 위한 변수. 1이 유지되면 'Yes', 0이면 'No'
final_result = 1

# 책의 번호를 배열에 저장하는 반복문
for i in range(M):
    num_books = int(input())
    data = list(map(int, input().split()))
    for j in range(num_books):
        array[i].append(data[j])

# 책의 맨 위 값을 확인하는 함수
# 만약 찾는 값이 있다면 배열에서 그 값을 pop() 으로 제거한다.
# x = 확인 할 수, array = 배열, M = 교과서 더미 수
def findNextNum(x, array, M):
    for i in range(M):
        if not array[i]:
            continue
        if array[i][-1] == x:
            result = 1
            array[i].pop()
            break
        else:
            result = 0
    return result

# 책더미의 맨 위에 1이 존배하는지를 확인하는 변수이다.
find_1 = findNextNum(1, array, M)

if find_1 == 0:
    final_result = 0
elif find_1 == 1:
    for i in range(2, N):
        find_num = findNextNum(i , array, M)
        if find_num == 0:
            final_result = 0
            break

if final_result == 0:
    print('No')
else:
    print('Yes')