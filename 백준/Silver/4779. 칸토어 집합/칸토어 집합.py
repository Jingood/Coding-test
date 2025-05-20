def solution(N):
    if N == 1:
        return "-"
    
    left = solution(N // 3)
    center = " " * (N // 3)
    return left + center + left


while True:
    try:
        N = int(input())

        answer = solution(3 ** N)
        print(answer)
    except:
        break