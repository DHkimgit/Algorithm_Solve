from itertools import combinations

t = int(input())

for i in range(t):
    boy, girl = map(int, input().split())
    boy_arr = [i for i in range(boy)]
    girl_arr = [i for i in range(girl)]

    # print(list(combinations(girl_arr, 2)))
    # print(list(combinations(boy_arr, 2)))

    # b1_result = boy * len(list(combinations(girl_arr, 2)))
    # g1_result = girl * len(list(combinations(boy_arr, 2)))

    # print(b1_result + g1_result)
    girl_temp = girl
    boy_temp = boy
    result_A = 0

    # (남1, 여2)인 경우
    while girl_temp > 2:
        girl_temp -= 2
        boy_temp -= 1
        result_A += 1
        if boy_temp == 0:
            break
    
    
    girl_temp = girl
    boy_temp = boy
    result_B = 0

    # (남2, 여1)인 경우
    while boy_temp > 2:
        boy_temp -= 2
        girl_temp -= 1
        result_B += 1
        if girl_temp == 0:
            break

    print(result_A + result_B)
    print(result_A)
    print(result_B)
# 8795 6340
# (남1 여2), (남2 여1)
# **구성된 팀의 개수**
# 여자(a, b, c, d) 4명일때 4c2(ab, ac, ad, bc, bd, cd) + 2c2 (1)
# 여자(a, b, c, d) 5명, 남자 2명 일때 
# 여자 5c2(ab, ac, ad, bc, bd, cd) + 남자1명/ 3c2 + 남자 1명 총 2팀 생성 가능
#  
# 남자 관점에서 2c1 + 여자 1명/ 총 1팀 생성 가능 답 2
# 남자3명(a, b, c) 여자 3명(c, d, f)
# 최대 몇 개의 조 ?
# 남자 1명 => 구성 할 수 있는 팀의 개수
# 10명 10명
# 10c2 + 1 / 8c2 + 1/ 6c2 + 1/ 4c2 + 1/ 2c2 + 1
# 남자 10명abcdefghuj 여자 10명ABCDEFGHIJ

# 만들수 있는 조의 최대 수 (남자로만, 여자로만은 불가능)
# (전부 여2 남1)
# ABa CDb EFc GHd IJe 5팀 생성
# 남자 5명 여자 10명
# 여2남1 여2남1 여2남1 여2남1 여2남1 5팀
# 남2여1 남2여1 여2남1 3팀
# 남1여2 남2여1 남1여2 남1여2 4팀
# 남자가 1명 있는 팀이 1개일때 최대 팀 수
# 남자가 1명 있는 팀이 2개일때 최대 팀 수
# 남자가 1명 있는 팀이 3개일때 최대 팀 수
# 남자가 1명 있는 팀이 4개일때 최대 팀 수
#
#
#
# 조만 만들면 된다
# ab/c + c/df
