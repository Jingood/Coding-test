N, M = map(int, input().split())
hands = list(map(int, input().split()))
answer = []

for i in range(len(hands)):
    for j in range(i + 1, len(hands) - 1):
        for k in range(j + 1, len(hands)):
            sum_num = hands[i] + hands[j] + hands[k]
            if sum_num <= M:
                answer.append(sum_num)
print(max(answer))