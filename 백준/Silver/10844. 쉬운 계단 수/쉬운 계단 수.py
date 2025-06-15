def count_stair_numbers(n):
    MOD = 1_000_000_000

    dp_cur = [0] * 10
    for d in range(1, 10):
        dp_cur[d] = 1
    
    for length in range(2, n + 1):
        dp_nxt = [0] * 10
        dp_nxt[0] = dp_cur[1]

        for d in range(1, 9):
            dp_nxt[d] = (dp_cur[d - 1] + dp_cur[d + 1]) % MOD
        dp_nxt[9] = dp_cur[8]

        dp_cur = dp_nxt

    return sum(dp_cur) % MOD



n = int(input())
print(count_stair_numbers(n))
