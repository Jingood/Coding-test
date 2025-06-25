from collections import deque

def solution(progresses, speeds):
    answer = []
    pro = deque(progresses)
    spd = deque(speeds)
    
    while pro:
        cnt = 0
        for i in range(len(pro)):
            pro[i] += spd[i]
            
        while pro and pro[0] >= 100:
            pro.popleft()
            spd.popleft()
            cnt += 1
        
        if cnt != 0:
            answer.append(cnt)
        
    return answer
