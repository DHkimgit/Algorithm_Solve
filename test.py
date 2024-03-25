def move_remote(num, broken):
    if num == 0:
        return -1 if broken[0] else 1
    
    length = 0
    while num > 0:
        if broken[num % 10]:
            return -1
        length += 1
        num //= 10
    return length

def main():
    n = int(input())  # 가고자 하는 채널
    m = int(input())  # 고장난 버튼의 개수
    broken_buttons = list(map(int, input().split()))  # 고장난 버튼
    
    broken = [False] * 10
    for button in broken_buttons:
        broken[button] = True
    print(broken)
    start = 100  # 초기 채널
    if n == start:
        print(0)
        return

    ans = abs(n - start)  # +/-로만 이동하는 경우
    for i in range(1000000):
        cnt = move_remote(i, broken)  # 숫자 버튼으로 가능한가?
        if cnt > 0:  # 숫자 버튼으로 이동 가능하면
            cnt += abs(n - i)  # 숫자 버튼으로 이동하고, +/- 이동
            ans = min(ans, cnt)  # 값이 더 작으면 업데이트
    
    print(ans)

if __name__ == "__main__":
    main()