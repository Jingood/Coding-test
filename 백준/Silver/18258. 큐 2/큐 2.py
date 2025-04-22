import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque()
out = []
for _ in range(N):
    cmd = input().split()
    op = cmd[0]

    if op == "push":
        queue.append(int(cmd[1]))
    
    elif op == "pop":
        out.append(str(queue.popleft() if queue else "-1"))
    
    elif op == "size":
        out.append(str(len(queue)))

    elif op == "empty":
        out.append("0" if queue else "1")

    elif op == "front":
        out.append(str(queue[0] if queue else "-1"))
    
    else:
        out.append(str(queue[-1] if queue else "-1"))

sys.stdout.write("\n".join(out))
            
