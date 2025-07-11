import sys

input = sys.stdin.readline

N = int(input())

distance = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
total_cost = 0

for i in range(N - 1):
    if price[i] < min_price:
        min_price = price[i]
    total_cost += min_price * distance[i]

print(total_cost)