import sys
N = int(sys.stdin.readline())

space = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
space.sort(key=lambda x:(x[1], x[0]))

for x, y in space:
    print(x, y)