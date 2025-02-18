Word = input().strip()
croatian_letters = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]

for letter in croatian_letters:
    Word = Word.replace(letter, '*')

print(len(Word))