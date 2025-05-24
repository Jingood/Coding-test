def dfs(s:list) -> list:
    if len(s) == M:
        print(" ".join(map(str, s)))
        return s
    
    for i in range(1, N + 1):
        s.append(i)
        dfs(s)
        s.pop()



N, M = map(int, input().split())
s = []

dfs(s)