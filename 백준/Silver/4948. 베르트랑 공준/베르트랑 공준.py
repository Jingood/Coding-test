def Eratostenes(n):
    prime = [True for _ in range((2 * n) + 1)]
    end = int((2 * n) ** 0.5) + 1

    prime[0] = False
    prime[1] = False

    for i in range(2, end):
        if prime[i]:
            for j in range(2 * i, (2 * n) + 1, i):
                prime[j] = False
    return prime

while True:
    N = int(input())
    cnt = 0
    if N == 0:
        break
    
    elif N == 1:
        print(1)

    else:
        prime = Eratostenes(N)
        for i in range(N + 1, 2 * N + 1):
            if prime[i]:
                cnt += 1
        print(cnt)


