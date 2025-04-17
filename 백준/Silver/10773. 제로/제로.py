import sys

stack, out = [], []
data = sys.stdin.read().split()
T = int(data[0])
nums = list(map(int, data[1:]))

for num in nums:
    if num == 0:
        stack.pop()

    else:
        stack.append(num)

out.append(str(sum(stack)))
sys.stdout.write('\n'.join(out))
