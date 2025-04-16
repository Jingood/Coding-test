import sys

input = sys.stdin.readline
T = int(input())
stack, out = [], []

for _ in range(T):
    cmd = input().split()
    op = cmd[0]

    if op == '1':
        stack.append(int(cmd[1]))

    elif op == '2':
        out.append(str(stack.pop()) if stack else '-1')
    
    elif op == '3':
        out.append(str(len(stack)))
    
    elif op == '4':
        out.append('1' if not stack else '0')
    
    else:
        out.append(str(stack[-1]) if stack else '-1')
    
sys.stdout.write("\n".join(out))