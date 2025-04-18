import sys

def check_matching(ps):
    stack = []

    for i in range(len(ps)):
        ch = ps[i]
        if ch == '(':
            stack.append(ch)
            continue
        else:
            if len(stack) == 0:
                return 0
            else:
                stack.pop()
                continue
    if len(stack) != 0:
        return 0
    return 1

data = sys.stdin.read().split()
T = int(data[0])
PS = list(data[1:])

out = []
for ps in PS:
    if check_matching(ps) == 1:
        out.append("YES")
    else:
        out.append("NO")

sys.stdout.write("\n".join(out))
