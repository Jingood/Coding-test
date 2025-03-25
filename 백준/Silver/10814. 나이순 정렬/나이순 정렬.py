import sys

N = int(sys.stdin.readline())

member = [list(sys.stdin.readline().split()) for _ in range(N)]

answer = sorted(member, key=lambda x:int(x[0]))
for m in answer:
    print(*m)