import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

cnt = [0] * M
cnt[0] = 1

current = 0
answer = 0

for num in nums:
    current = (current + num) % M
    answer += cnt[current]
    cnt[current] += 1

print(answer)