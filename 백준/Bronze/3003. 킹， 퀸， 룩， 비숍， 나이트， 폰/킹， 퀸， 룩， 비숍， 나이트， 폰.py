White_list = list(map(int, input().split()))
Comp = [1, 1, 2, 2, 2, 8]
answer = [Comp[i] - White_list[i] for i in range(0, len(White_list))]
print(*answer)