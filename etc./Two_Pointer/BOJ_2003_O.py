N, M = map(int, input().split())

arr = list(map(int, input().split()))

interval_sum = 0

count = 0

end = 0

for start in range(N):
    while interval_sum < M and end < N:
        interval_sum = interval_sum + arr[end]
        end = end + 1
    if interval_sum == M:
        count += 1
    
    interval_sum = interval_sum - arr[start]

print(count)

"""
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 
이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

##투포인터 알고리즘##
배열이나 문자열같은 선형 구조에서 각자 다른 원소를 가리키는 2개의 포인터를 조작해가면서 원하는 것을 얻어내는 알고리즘

이 문제의 경우 이중루프문을 이용해 모든 경우의수를 탐색하며 답을 구할 수 있지만 (브루트 포스법) 이 경우 시간복잡도가 O(N^2)
이 되버린다.

이 문제의 경우 start포인터와 end 포인터가 0 인 상태에서
부분합이 목표치에 다다를때까지 end 포인터를 증가시키면서 부분합을 구한다.
부분합이 목표치에 도달하면 count변수에 값을 추가하고 start 포인터가 가르키고 있는 지점을 부분합에서 뺀 뒤
start 포인터를 1 증가시켜서 다시 일련의 과정을 반복한다.

모든 배열의 값이 자연수 이므로 end 포인터가 증가함에 따라 부분합 또한 당연히 증가하게 된다. 이 과정에서 부분합이
목표치를 초과하면 맨 뒤에 있는 start 포인터가 가르키고 있는 배열의 원소를 부분합에서 빼는 원리이다.

"""