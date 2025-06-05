import sys

input = sys.stdin.readline

def check(y: int, x: int, check_num: int) -> bool:
    for i in range(9):
        if sudoko[y][i] == check_num or sudoko[i][x] == check_num:
            return False
    
    for i in range(3):
        for j in range(3):
            if sudoko[(y // 3) * 3 + i][(x // 3) * 3 + j] == check_num:
                return False
    return True

def dfs(n: int):
    if n == len(blank):
        for i in sudoko:
            print(*i)
        exit()
    
    for check_num in range(1, 10):
        y, x = blank[n]

        if check(y, x, check_num):
            sudoko[y][x] = check_num
            dfs(n + 1)
            sudoko[y][x] = 0


sudoko = [list(map(int, input().split())) for _ in range(9)]
blank = [(i, j) for i in range(9) for j in range(9) if sudoko[i][j] == 0]

dfs(0)