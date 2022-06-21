N = int(input())
S = list(map(int, input().split()))

ypriceSum = 0
mPriceSum = 0

yPriceQ = 0
mPriceQ = 0

for i in range(N):
    yPriceQ = S[i] //30
    if(yPriceQ == 0):
        ypriceSum = ypriceSum + 10
    else:
        ypriceSum = ypriceSum + (yPriceQ + 1) * 10

for i in range(N):
    mPriceQ = S[i] //60
    if(mPriceQ == 0):
        mPriceSum = mPriceSum + 15
    else:
        mPriceSum = mPriceSum + (mPriceQ + 1) * 15

if(ypriceSum > mPriceSum):
    print('M', mPriceSum)
elif(ypriceSum < mPriceSum):
    print('Y', ypriceSum)
else:
    print('Y', 'M', ypriceSum)
