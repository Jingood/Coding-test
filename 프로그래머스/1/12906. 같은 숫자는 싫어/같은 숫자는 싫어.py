from collections import deque

def solution(arr):
    queue = deque(arr)
    answer = []
    if queue:
        prev = queue.popleft()
        answer.append(prev)
        while queue:
            current = queue.popleft()
            if current != prev:
                answer.append(current)
                prev = current
    return answer