import sys

input = sys.stdin.readline

N, K = map(int, input().split())

nums = list(map(int, input().split()))

current_sum = sum(nums[:K])
max_sum = current_sum

for i in range(K, N):
    current_sum += nums[i]
    current_sum -= nums[i - K]
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)
