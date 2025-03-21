import sys
N = int(sys.stdin.readline())
space = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

space.sort()
for n in space:
    print(n[0], n[1])
