def solution(myString, pat):
    answer = 0
    plen = len(pat)
    for i in range(0, len(myString)):
        if myString[i:plen + i] == pat:
            answer += 1
    return answer