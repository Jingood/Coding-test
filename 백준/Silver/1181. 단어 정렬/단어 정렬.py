import sys

N = int(sys.stdin.readline())

Str = [sys.stdin.readline().strip() for _ in range(N)]
Str = set(Str)
Str = list(Str)
Str.sort()
Str.sort(key=len)

for s in Str:
    print(s)
