import sys
 
input = sys.stdin.readline

N = int(input())

person = []
cnt = 0
for _ in range(N):
    chat = input().strip()
    if chat == 'ENTER':
        temp = set(person)
        cnt += len(temp)
        person.clear()
    
    else:
        person.append(chat)

person = set(person)
cnt += len(person)
print(cnt)