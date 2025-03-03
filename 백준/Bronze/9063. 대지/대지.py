N = int(input())

vector = [list(map(int, input().split())) for _ in range(N)]

x = []
y = []

for r, c in vector:
    x.append(r)
    y.append(c)

d = max(x) - min(x)
h = max(y) - min(y)
print(d * h)