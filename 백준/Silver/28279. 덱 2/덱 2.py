import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

deq = deque()
out = []

for _ in range(N):
    cmd = input().split()
    op = int(cmd[0])

    if op == 1:
        deq.appendleft(int(cmd[1]))
    
    elif op == 2:
        deq.append(int(cmd[1]))
    
    elif op == 3:
        out.append(str(deq.popleft() if deq else "-1"))
    
    elif op == 4:
        out.append(str(deq.pop() if deq else "-1"))
    
    elif op == 5:
        out.append(str(len(deq)))
    
    elif op == 6:
        out.append("0" if deq else "1")
    
    elif op == 7:
        out.append(str(deq[0] if deq else "-1"))
    
    else:
        out.append(str(deq[-1] if deq else "-1"))

sys.stdout.write("\n".join(out))
sys.stdout.write("\n")
