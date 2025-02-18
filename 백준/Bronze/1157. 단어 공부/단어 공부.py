Word = input().strip().upper()
freq = {}
for char in Word:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
max_count = 0
max_char = ''
for char, count in freq.items():
    if count > max_count:
        max_count = count
        max_char = char
tie = 0
for count in freq.values():
    if count == max_count:
        tie += 1
if tie > 1:
    answer = "?"
else:
    answer = max_char.upper()
print(answer)