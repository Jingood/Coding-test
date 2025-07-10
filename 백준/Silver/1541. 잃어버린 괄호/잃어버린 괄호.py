import sys

input = sys.stdin.readline

def minimal(expr):
    parts = expr.split('-')
    parts_sum = [sum(map(int, part.split('+'))) for part in parts]
    return parts_sum[0] - sum(parts_sum[1:])

expr = input().strip()
print(minimal(expr))