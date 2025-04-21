import sys

N = sys.stdin.readline()

people = list(map(int, sys.stdin.readline().split()))

stack = []
now_turn = 1

for person in people:
    stack.append(person)

    while stack and stack[-1] == now_turn:
        temp = stack.pop()
        now_turn += 1

if stack:
    print("Sad")
else:
    print("Nice")


