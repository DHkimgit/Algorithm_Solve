import random

answer = random.randrange(0, 100)

min_hint = 0
max_hint = 99

for i in range(10):
    print(f'숫자를 입력하세요(범위:{min_hint}~{max_hint}): ', end='')
    guess = int(input())
    if guess == answer:
        print(f' 정답입니다. {i+1}번 만에 맞추셨습니다.')
        break
    elif guess > answer:
        print(' 아닙니다. 더 작은 숫자입니다!')
        max_hint = guess - 1
    else:
        print(' 아닙니다. 더 큰 숫자입니다!')
        min_hint = guess + 1

print(' 게임이 끝났습니다.')