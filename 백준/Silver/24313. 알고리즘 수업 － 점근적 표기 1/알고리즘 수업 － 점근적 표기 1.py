a, b = map(int, input().split())
c = int(input())
n = int(input())

f = (a * n) + b
g = c * n

if a < c:
    if (a - c) * n + b <= 0:
        print(1)
    else:
        print(0)

elif a == c:
    if b <= 0:
        print(1)
    else:
        print(0)

elif a > c:
    print(0)