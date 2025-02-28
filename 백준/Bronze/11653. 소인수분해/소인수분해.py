N = int(input())
k = 2

if N == 1:
    print()

while N > 1:
    if N % k == 0:
        print(k)
        N = N // k
    
    else:
        k += 1