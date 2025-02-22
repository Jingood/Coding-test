T = int(input())


for _ in range(T):
    C = int(input())
    Cent = [0, 0, 0, 0]
    while C > 0:
        if C >= 25:
            C = C - 25
            Cent[0] += 1
        elif 25 > C >= 10:
            C = C - 10
            Cent[1] += 1
        elif 10 > C >= 5:
            C = C - 5
            Cent[2] += 1
        else:
            C = C - 1
            Cent[3] += 1
    print(* Cent)