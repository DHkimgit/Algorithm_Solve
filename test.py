import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [0]*(n+1)
for _ in range(m):
    bookNum = int(input())
    books = list(map(int, input().split()))
    for i in range(bookNum-1):
        if books[i] < books[i+1]:
            print("No")
            exit(0)
print("Yes")