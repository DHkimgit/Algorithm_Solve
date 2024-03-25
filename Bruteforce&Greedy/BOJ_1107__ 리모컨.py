from itertools import product
N = int(input())
M = int(input())

if M == 0 or N == 100:
    if N != 100:
        print(min(len(str(N)), abs(N - 100)))
    else:
        broke = list(map(int, input().split()))
        print(0)

elif M == 10:
    broke = list(map(int, input().split()))
    print(abs(N - 100))

else:
    broke = list(map(int, input().split()))
    remote = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    normal = [x for x in remote if x not in broke] # 사용 가능한 리모컨 버튼
    normal.sort()
    
    N_str = str(N)
    length_N = len(N_str)

    first_N = N_str[0] # N의 첫째 자리 수

    table = [] # 생성 가능한 모든 체널을 경우의 수를 저장할 배열

    all_combinations = product(*([normal]+ [normal] * (length_N - 1)))

    table = [''.join(map(str, comb)) for comb in all_combinations]
    
    if length_N >= 1 and len(normal) >= 1:
        if normal[0] == 0 and len(normal) >= 2:
            t = str(normal[1])
            for i in range(length_N):
                t += str(0)
        else:
            t = str(normal[0])
            for i in range(length_N):
                t += str(normal[0])
        table.append(str(t))
        
        if length_N >= 2:
            max_normal = max(normal)
            k = str(max_normal)
            for i in range(length_N - 2):
                k += str(max_normal)
            table.append(str(k))

    minch = 9999999
    index = 0
    indexes = []

    for i in range(len(table)):
        if minch >= abs(N - int(table[i])):
                minch = abs(N - int(table[i]))
                index = i

    for i in range(len(table)):
        if minch == abs(N - int(table[i])):
            indexes.append(i)   

    if minch >= abs(N - int(table[-1])) and len(table) >= 3:
        print(min((minch + len(table[-1])), abs(N - 100)))

    elif N - minch == 0:
        tmp = int(table[index])
        print(min((minch + len(str(tmp))), abs(N - 100)))

    else:
        results = []
        if len(indexes) != 1:
            for i in range(len(indexes)):
                results.append(minch + len(table[indexes[i]]))
            print(min((min(results)), abs(N - 100)))

        else:
            print(min((minch + len(table[index])), abs(N - 100)))






    # close_first_button_tmp = []

    # close_first_button = [] #브루트포스 돌릴 N과 가장 가까운 수 중 가장 왼쪽 자리 수 결정
    
    # for i in range(len(normal)):
    #     close_first_button_tmp.append(abs(int(first_N) - normal[i]))
    # min_tmp = min(close_first_button_tmp)
    # for i in range(len(close_first_button_tmp)):
    #     if close_first_button_tmp[i] == min_tmp:
    #         close_first_button.append(normal[i])