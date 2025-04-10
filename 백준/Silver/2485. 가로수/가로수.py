import sys

def Euclidean(a, b):
    if b == 0:
        return a
    return Euclidean(b, a % b)

N = int(sys.stdin.readline())

tree = []
sub = []
cnt = 0
for _ in range(N):
    n = int(sys.stdin.readline())
    tree.append(n)

for i in range(N-1):
    s = tree[i + 1] - tree[i]
    sub.append(s)

gcd = sub[0]
for j in range(1, len(sub)):
    gcd = Euclidean(gcd, sub[j])

for k in sub:
    cnt += (k // gcd) - 1
print(cnt)



