cu, du = map(int, input().split())
cd, dd = map(int, input().split())
cp, dp = map(int, input().split())
pinkbinHp = int(input())
second = 1
pinkbinHp = pinkbinHp - du - dd - dp

while(pinkbinHp > 0):
    
    if second % cu == 0 and cu >= second:
        pinkbinHp -= du

    if second % cd == 0 and cu >= second:
        pinkbinHp -= dd

    if second % cp == 0 and cu >= second:
        pinkbinHp -= dp

    second += 1

print(second - 1)