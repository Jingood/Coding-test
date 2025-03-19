import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    n = int(sys.stdin.readline())
    arr.append(n)

arr.sort()
print(*arr, sep='\n')