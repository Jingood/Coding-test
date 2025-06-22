import sys

input = sys.stdin.readline

n = int(input())

lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort(key=lambda pair: pair[0])

B = [pair[1] for pair in lines]
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if B[j] < B[i]:
            dp[i] = max(dp[i], dp[j] + 1)

LIS_length = max(dp)
answer = n - LIS_length
print(answer)