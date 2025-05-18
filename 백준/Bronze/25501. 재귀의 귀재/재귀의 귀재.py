import sys

def Recursion(s: chr, l: int, r: int, c: int)->int:
    if l >= r:
        return 1, c
    elif s[l] != s[r]:
        return 0, c
    else:
        return Recursion(s, l + 1, r - 1, c + 1)
    
def IsPalindrome(s: chr):
    return Recursion(s, 0, len(s) - 1, 1)

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = input().strip()
    a, b = IsPalindrome(s)
    print(a, b)