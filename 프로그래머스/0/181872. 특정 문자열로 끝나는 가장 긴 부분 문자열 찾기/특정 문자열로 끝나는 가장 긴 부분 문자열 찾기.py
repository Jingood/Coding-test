def solution(myString, pat):
    answer = ''
    last_index = myString.rfind(pat)
    answer += myString[:last_index + len(pat)]        
    return answer