N = int(input())
min_bags = float('inf')

for count5 in range(N // 5 + 1):
    for count3 in range(N // 3 + 1):
        if 5 * count5 + 3 * count3 == N:
            min_bags = min(min_bags, count5 + count3)

if min_bags == float('inf'):
    print(-1)
else:
    print(min_bags)