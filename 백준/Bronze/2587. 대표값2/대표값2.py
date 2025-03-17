arr = []

for _ in range(5):
    n = int(input())
    arr.append(n)

num = sorted(arr)
mean = sum(num) // 5
mid = num[2]
print(mean)
print(mid)