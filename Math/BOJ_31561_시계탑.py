M = int(input())

if M <= 30:
    print(float(M/2))

else:
    K = M - 30
    print(float(15 + ((K * 3) / 2)))