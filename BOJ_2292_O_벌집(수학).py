N = int(input())
i = 1
end = 1

while N > end:
    end = end + 6*i
    i += 1
    
if N != 1:
    print(i)
else:
    print(1)
