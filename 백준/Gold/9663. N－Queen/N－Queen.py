import sys

def check(now_row: int) -> bool:
    for row in range(now_row):
        if visited[now_row] == visited[row] or (now_row - row) == abs(visited[now_row] - visited[row]):
            return False
    return True


def dfs(row):
    global cnt

    if row == N:
        cnt += 1
        return
    
    else:
        for col in range(N):
            visited[row] = col
            if check(row):
                dfs(row + 1)

input = sys.stdin.readline
N = int(input())

visited = [-1] * N
cnt = 0

dfs(0)
print(cnt)