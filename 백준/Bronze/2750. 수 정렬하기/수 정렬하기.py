N = int(input())
arr = []

for _ in range(N):
    n = int(input())
    arr.append(n)

s_arr = sorted(arr)
for i in s_arr:
    print(i)