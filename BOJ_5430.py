import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    order = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(","))

    if n == 0:
        arr = deque()
    
    reverse_flag = False
    error_flag = False

    for i in order:
        if i == 'R' and reverse_flag == False:
            reverse_flag = True
        elif i == 'R' and reverse_flag == True:
            reverse_flag = False
        elif i == 'D':
            if len(arr) < 1:
                error_flag = True
                break
            if reverse_flag:
                arr.pop()
            else:
                arr.popleft()
    
    if error_flag:
        print('error')
    else:
        if reverse_flag:
            arr.reverse()
        result = str(list(map(int, arr))).replace(' ', '')
        print(result)














# T = int(input())

# for i in range(T):
#     result = ''
#     order = input()
#     n = int(input())
#     input_arr = input()
#     if n == 0:
#         print('ERROR')
#         continue
#     else:
#         arr = list(map(int, input_arr.strip('[]').split(',')))

#     for i in range(len(order)):
#         if order[i] == 'D':
#             if len(arr) == 0:
#                 result = 'ERROR'
#                 break
#             arr.pop(0)
#         elif order[i] == 'R':
#             arr.reverse()
#     if result != 'ERROR':
#         result = str(arr).strip()
#     print(result)