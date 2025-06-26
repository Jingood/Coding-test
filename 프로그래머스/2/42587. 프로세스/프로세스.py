from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque((p, i) for i, p in enumerate(priorities))
    
    while queue:
        p, idx = queue.popleft()
        
        if any(p2 > p for p2, _ in queue):
            queue.append((p, idx))
        else:
            answer += 1
            if idx == location:
                return answer