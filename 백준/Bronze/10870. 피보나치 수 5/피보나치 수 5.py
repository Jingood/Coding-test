def Fibonacci(N: int)->int:
    if N <= 1:
        return N
    return Fibonacci(N - 1) + Fibonacci(N - 2)


N = int(input())
print(Fibonacci(N))

