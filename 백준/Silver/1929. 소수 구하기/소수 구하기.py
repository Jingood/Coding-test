import sys

def Eratostenes(n):
        prime = [True for i in range(n + 1)]
        end = int(n ** 0.5) + 1

        prime[1] = False

        for j in range(2, end):
            if prime[j]:
                  for k in range(2 * j, n + 1, j):
                        prime[k] = False
        return prime


M, N = map(int, sys.stdin.readline().split())

prime = Eratostenes(N)
for i in range(M, N + 1):
      if prime[i]:
            print(i)

