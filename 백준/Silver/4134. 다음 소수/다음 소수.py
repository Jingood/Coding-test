import sys

T = int(sys.stdin.readline())

def check(n):
    nums = int(n ** 0.5) + 1
    for num in range(2, nums):
        if n % num == 0:
            return False
    return True

for _ in range(T):
    n = int(sys.stdin.readline())
    while True:
        if n == 0 or n == 1:
            print(2)
            break
        else:
            if check(n):
                print(n)
                break
            else:
                n += 1