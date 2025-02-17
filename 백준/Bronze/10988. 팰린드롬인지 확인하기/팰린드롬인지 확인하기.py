Word = list(input())
Wlen = len(Word)
answer = 1
for i in range(0, Wlen // 2):
    if (Word[i]) != (Word[Wlen - 1 - i]):
        answer = 0
        break
print(answer)