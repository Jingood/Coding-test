import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
number = list(map(int, input().split()))
balloon = deque(i for i in range(1, N + 1))
out = []

while balloon:
    n = balloon.popleft()
    out.append(str(n))
    r = number[n - 1]
    step = r - 1 if r > 0 else r
    balloon.rotate(-step)

sys.stdout.write(" ".join(out))
sys.stdout.write("\n")
    
