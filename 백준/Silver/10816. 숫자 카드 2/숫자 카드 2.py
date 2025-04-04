import sys

N = int(sys.stdin.readline())

cards = list(map(int, sys.stdin.readline().split()))
counts = {}

for card in cards:
    if card in counts:
        counts[card] += 1
    else:
        counts[card] = 1

M = int(sys.stdin.readline())

comp = list(map(int, sys.stdin.readline().split()))

for c in comp:
    if c in counts:
        print(counts[c], end=" ")
    else:
        print(0, end=" ")