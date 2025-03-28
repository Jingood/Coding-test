import sys

N, M = map(int, sys.stdin.readline().split())

S = {sys.stdin.readline().strip() : 1 for _ in range(N)}

checks = list(sys.stdin.readline().strip() for _ in range(M))

cnt = 0
for i in range(M):
    if checks[i] in S:
        cnt += 1

print(cnt)