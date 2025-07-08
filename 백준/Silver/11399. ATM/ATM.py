import sys

input = sys.stdin.readline

N = int(input())

waitting = list(map(int, input().split()))

waitting.sort()

time = [0] * (N + 1)

for i in range(1, N + 1):
    time[i] = time[i - 1] + waitting[i - 1]

print(sum(time))