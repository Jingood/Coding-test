# 색종이_만들기.py

import sys

# 재귀 함수 정의
def solve(x, y, n):
    global white_count, blue_count

    # 현재 영역의 첫 번째 칸의 색을 기준으로 잡음
    color = paper[x][y]
    
    # 현재 영역이 모두 같은 색인지 확인
    all_same_color = True
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                all_same_color = False
                break
        if not all_same_color:
            break

    # 만약 모두 같은 색이라면 해당 색종이 개수 증가
    if all_same_color:
        if color == 0: # 하얀색
            white_count += 1
        else: # 파란색
            blue_count += 1
    else:
        # 같은 색이 아니라면 4등분하여 재귀 호출
        half = n // 2
        solve(x, y, half)             # 왼쪽 위
        solve(x, y + half, half)      # 오른쪽 위
        solve(x + half, y, half)      # 왼쪽 아래
        solve(x + half, y + half, half) # 오른쪽 아래

# 전역 변수 초기화
white_count = 0
blue_count = 0

# 입력 처리
N = int(sys.stdin.readline())
paper = []
for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

# 함수 호출
solve(0, 0, N)

# 결과 출력
print(white_count)
print(blue_count)
