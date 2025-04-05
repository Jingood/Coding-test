import sys

N, M = map(int, sys.stdin.readline().split())
listen = {sys.stdin.readline().strip() : 1 for _ in range(N)}
watch = [sys.stdin.readline().strip() for _ in range(M)]
no = []
for w in watch:
    if w in listen:
        no.append(w)
no.sort()
print(len(no))
print(*no, sep="\n")
