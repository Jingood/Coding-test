def factorial(N: int, ans: int) -> int: 
    if N == 0:
        return ans
    
    return factorial(N - 1, ans * N)

N = int(input())

print(factorial(N, 1))