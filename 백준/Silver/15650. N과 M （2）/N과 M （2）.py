def dfs(start: int):
    if len(s) == M:
        print(" ".join(map(str, s)))
    
    for i in range(start, N + 1):
        if i not in s:
            s.append(i)
            dfs(i + 1)
            s.pop()

N, M = map(int, input().split())
s =[]

dfs(1)
