import sys


def dfs(L, idx):
    global res
    if L == n // 2:
        A = 0
        B = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    A += team[i][j]
                elif not visited[i] and not visited[j]:
                    B += team[i][j]
        res = min(res, abs(A - B))
        return
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(L + 1, i + 1)
            visited[i] = False

input = sys.stdin.readline

n = int(input())
team = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]

res = 2147000
dfs(0, 0)
print(res)