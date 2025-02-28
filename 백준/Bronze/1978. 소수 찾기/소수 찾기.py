N = int(input())

arr = list(map(int, input().split()))
answer = N

for i in arr:
    if i == 1:
        answer -= 1
    else:
        for j in range(2, i):
            if i % j == 0:
                answer -= 1
                break

print(answer)