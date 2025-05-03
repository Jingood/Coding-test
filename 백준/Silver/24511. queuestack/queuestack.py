import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

qs = list(map(int, input().split()))
init = list(map(int, input().split()))

M = int(input())
nums = list(map(int, input().split()))

out = []

queue_positions = [i for i, t in enumerate(qs) if t == 0]
queue_vals = deque(init[i] for i in queue_positions)


if queue_vals:
    for x0 in nums:
        queue_vals.appendleft(x0)
        xN = queue_vals.pop()
        out.append(str(xN))

else:
    out = list(map(str, nums))


sys.stdout.write(" ".join(out))
sys.stdout.write("\n")
