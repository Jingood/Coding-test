import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [input().rstrip() for _ in range(N)]

SUM = [[0]*(M+1) for _ in range(N+1)]
for i in range(N):
    prev = SUM[i]
    curr = SUM[i+1]
    brow = board[i]
    for j in range(M):
        need = ((i+j)&1) ^ (brow[j]=='W')
        curr[j+1] = prev[j+1] + curr[j] - prev[j] + need


ans = N*M  
K2  = K*K
SUM_local = SUM
limit_r = N+1
limit_c = M+1

for r in range(K, limit_r):
    row_r   = SUM_local[r]
    row_rk  = SUM_local[r-K]
    for c in range(K, limit_c):
        x = row_r[c] - row_rk[c] - row_r[c-K] + row_rk[c-K]
        if x < ans:       ans = x
        if K2-x < ans:    ans = K2-x
    if ans == 0:
        break

print(ans)