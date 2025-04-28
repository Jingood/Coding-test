import sys
from collections import deque

N, K = map(int, input().split())

circle = deque(i for i in range(1, N + 1))
out = []

while circle:
    circle.rotate(-(K - 1))
    item = circle.popleft()
    out.append(str(item))
sys.stdout.write("<")
sys.stdout.write(", ".join(out))
sys.stdout.write(">\n")


