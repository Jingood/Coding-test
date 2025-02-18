N = int(input())
answer = 0
for _ in range(0, N):
    cnt = 0
    Word = list(input())
    if len(Word) == 1 or len(Word) == 2:
        answer += 1
    
    else:
        for i in range(len(Word)-1, 1, -1):
            Comp = Word[i]
            for j in range(i - 2, -1, -1):
                if(Comp != Word[i - 1] and Comp == Word[j]):
                    cnt += 1
        if cnt == 0:
            answer += 1
print(answer) 


 