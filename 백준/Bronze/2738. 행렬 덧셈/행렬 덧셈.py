N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
C = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        C[i][j] = A[i][j] + B[i][j]

for k in range(N):
    print(*C[k])