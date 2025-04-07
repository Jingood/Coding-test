import sys

S = sys.stdin.readline().strip()

total = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        total.add(S[i:j+1])
print(len(total))
