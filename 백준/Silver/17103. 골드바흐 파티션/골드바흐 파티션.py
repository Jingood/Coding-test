import sys

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    end = int(limit ** 0.5) + 1

    for i in range(2, end):
        if is_prime[i]:
            for multiple in range(i * i, limit + 1, i):
                is_prime[multiple] = False
    
    primes = []
    for j in range(limit + 1):
        if is_prime[j]:
            primes.append(j)
    return is_prime, primes

def count_pairs(n, primes):
    l, r = 0, len(primes) - 1
    while r >=0 and primes[r] > n:
        r -= 1
    
    ans = 0
    while l <= r:
        s = primes[l] + primes[r]
        if s == n:
            l += 1
            r -= 1
            ans += 1

        elif s < n:
            l += 1 
        
        else:
            r -= 1
    return ans

data = sys.stdin.read().split()
T = int(data[0])
nums = list(map(int, data[1:]))
max_n = max(nums) 
_, primes = sieve(max_n)

out = []
for n in nums:
    out.append(str(count_pairs(n, primes)))
sys.stdout.write("\n".join(out))
