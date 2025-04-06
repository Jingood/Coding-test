import sys

cnt = 0
a, b = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

temp = {}

for i in A:
    if i not in temp:
        temp[i] = 1

for j in B:
    if j not in temp:
        temp[j] = 1
    else:
        del temp[j]

print(len(temp))