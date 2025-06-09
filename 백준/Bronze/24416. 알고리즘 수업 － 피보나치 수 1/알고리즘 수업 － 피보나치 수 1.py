def fibonacci(n: int) -> int:
    return n - 2

def fibo(n: int) -> int:
    global f
    f[0] = f[1] = 1
    for i in range(3, n):
        f[i] = f[i - 1] + f[i - 2]
    return f[n - 1]

n = int(input())
f = [i for i in range(n)]

print(fibo(n), fibonacci(n))