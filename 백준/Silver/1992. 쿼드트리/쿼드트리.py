import sys

input = sys.stdin.readline

def quadtree(x, y, n):
    global result

    color = video[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != video[i][j]:
                result.append("(")
                quadtree(x, y, n // 2)
                quadtree(x, y + (n // 2), n // 2)
                quadtree(x + (n // 2), y, n // 2)
                quadtree(x + (n // 2), y + (n // 2), n // 2)
                result.append(")")
                return
    result.append(color)

N = int(input())
video = [list(map(int, input().rstrip())) for _ in range(N)]
result = []

quadtree(0, 0, N)
sys.stdout.write("".join(map(str, result)))