length = int(input())
qraph = [[0 for x in range(length)] for x in range(length)]
print(qraph)
# from itertools import combinations

# l,c = map(int,input().split()) 
# word = sorted(list(map(str,input().split()))) 

# m = ['a','e','i','o','u']


# def cnt(password):
#     result = []
#     mm = 0  # 모음 갯수
#     zz = 0  # 자음 갯수
#     for i in range(l):
#         if password[i] in m:
#             mm += 1
#         else:
#             zz += 1
#     result.append(mm)
#     result.append(zz)
#     return result

# example = list(combinations(word,l))  # 모든 경우

# final = [] # 모든 경우를 cnt함수에 넣은 결과가 들어간 리스트
# for i in range(len(example)):
#     final.append(cnt(example[i]))

# finals = []  # 모음이 1개이상, 자음이 2개 이상인 조건을 만족하는 경우를 저장하는 리스트
# for i in range(len(final)):
#     if final[i][0] >= 1 and final[i][1] >= 2:
#         finals.append(list(example[i]))  # 튜플을 리스트로 변경
# for i in range(len(finals)):
#     print("".join(finals[i]))