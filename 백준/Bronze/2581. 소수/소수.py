M = int(input())
N = int(input())

arr = [i for i in range(M, N + 1)]


if 1 in arr:
    arr.remove(1)

for num in arr[:]:
    for j in range(2, num):
        if num % j == 0:
            arr.remove(num)
            break

if len(arr) == 0:
    print(-1)

else: 
    Sumnum = sum(arr)
    Minnum = min(arr)
    print(Sumnum)
    print(Minnum)