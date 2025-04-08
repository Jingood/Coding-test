import sys, math

T = int(sys.stdin.readline())

for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    print(math.lcm(n, m))
    
