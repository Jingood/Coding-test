def change(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        if mod < 10:
            rev_base += str(mod)
        else:
            rev_base += chr(ord('A') + mod - 10)
    
    return rev_base[::-1]


N, B = map(int,input().split())

print(change(N, B))
