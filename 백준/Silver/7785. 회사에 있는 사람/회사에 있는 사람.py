import sys

N = int(sys.stdin.readline())

temp = dict()

for _ in range(N):
    a, b = sys.stdin.readline().split()
    if b == "enter":
        temp[a] = b
    else:
        del temp[a]

temp = sorted(temp.keys(), reverse=True)
for i in temp:
    print(i)