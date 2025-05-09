def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

N, K = map(int, input().split())

print(factorial(N) // (factorial(N - K) * factorial(K)))

