import sys

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

input = sys.stdin.readline
T = int(input())
out = []
for _ in range(T):
    N, M = map(int, input().split())
    count = factorial(M) // (factorial(M - N) * factorial(N))
    out.append(str(count))

sys.stdout.write("\n".join(out))

