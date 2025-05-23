import sys

input = sys.stdin.readline

N, M = map(int, input().split())
words = {}

for _ in range(N):
    word = input().strip()

    if len(word) >= M:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

Memo = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for m in Memo:
    print(m[0])


