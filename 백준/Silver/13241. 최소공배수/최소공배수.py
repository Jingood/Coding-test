import sys

def Euclidean(a, b):
    if b == 0:
        return a
    return Euclidean(b, a % b)

A, B = map(int, sys.stdin.readline().split())
gcd = Euclidean(A, B)
lcm = (A * B) // gcd
print(lcm)