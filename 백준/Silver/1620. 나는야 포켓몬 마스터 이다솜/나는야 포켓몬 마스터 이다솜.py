import sys

N, M = map(int, sys.stdin.readline().split())

poke = {sys.stdin.readline().strip() : i for i in range(1, N + 1)}
poke_s = {idx : n for n, idx in poke.items()}

prob = [sys.stdin.readline().strip() for _ in range(M)]

for p in prob:
    if p.isdigit():
        print(poke_s[int(p)])
    else:
        print(poke[p])
