x, y, w, h = map(int, input().split())

row_r = w - x
col_u = h - y

if row_r <= col_u:
    if row_r <= y and row_r <= x:
        print(row_r)
    elif y < row_r and y <= x:
        print(y)
    else:
        print(x)
else:
    if col_u <= y and col_u <= x:
        print(col_u)
    elif y < col_u and y <= x:
        print(y)
    else:
        print(x)