def hanoi(N: int, start: int, end: int, assi: int)->None:
    if N == 1:
        print(start, end)
        return
    hanoi(N - 1, start, assi, end)
    print(start, end)
    hanoi(N - 1, assi, end, start)


N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 3, 2)