# 남자 3명 여자 3명
# 남자가 1명 있는 팀이 1개일때 최대 팀 수 남1 여2 + 남2 여1
# 남자가 1명 있는 팀이 2개일때 최대 팀 수
# 남자가 1명 있는 팀이 3개일때 최대 팀 수
t = int(input())

for i in range(t):
    boy, girl = map(int, input().split())
    maxteam = 0
    
    for j in range(1, boy + 1):
        boy_tmp = boy
        girl_tmp = girl
        boy_tmp -= j
        girl_tmp -= 2*j
        if girl_tmp <= 0:
            continue
        result = j

        while boy_tmp >= 2:
            boy_tmp -= 2
            girl_tmp -= 1
            result += 1
            if girl_tmp == 0:
                break
        
        if result < maxteam:
            break

        maxteam = max(maxteam, result)

    print(maxteam)
        




