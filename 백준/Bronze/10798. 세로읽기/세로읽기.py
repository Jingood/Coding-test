Word = [list(input()) for _ in range(5)]
Word_list = []
max_len = max(len(w) for w in Word)

for j in range(max_len):
    for i in range(5):
        if j < len(Word[i]):
            Word_list.append(Word[i][j])

print("".join(Word_list))