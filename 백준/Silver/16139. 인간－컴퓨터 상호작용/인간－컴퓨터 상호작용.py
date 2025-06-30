import sys

input = sys.stdin.readline

S = input().strip()
q = int(input())

out = [0] * q
i = 0

while i < q:
    a, l, r = input().split()
    l, r = map(int, (l, r))

    for s in S[l:r + 1]:
        if s == a:
            out[i] += 1
    i += 1


for i in out:
    print(i)