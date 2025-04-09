import sys, math

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

d = B * D
u = (A * D) + (C * B)
k = math.gcd(d, u)

print(u // k, d // k)

