from collections import deque

N = int(input())

d = deque()

for i in range(1, N + 1):
    d.append(i)

while True:
    if len(d) == 1:
        ans = d.popleft()
        break

    d.popleft()
    d.rotate(-1)

print(ans)
