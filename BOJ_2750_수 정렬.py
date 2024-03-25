N = int(input())
array = []

for i in range(N): 
    tmp = int(input())
    array.append(tmp)
   
array.sort()
for i in array: 
	print(i)