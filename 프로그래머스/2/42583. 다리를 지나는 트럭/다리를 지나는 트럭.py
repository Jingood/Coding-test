from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    total_weight = 0
    last_load_time = 0

    for tw in truck_weights:
        load_time = last_load_time + 1

        while bridge and bridge[0][0] <= load_time:
            exit_time, w = bridge.popleft()
            total_weight -= w

        while total_weight + tw > weight or len(bridge) >= bridge_length:
            next_exit_time, w = bridge.popleft()
            total_weight -= w
            load_time = next_exit_time
            while bridge and bridge[0][0] <= load_time:
                exit_time, w = bridge.popleft()
                total_weight -= w

        exit_time = load_time + bridge_length
        bridge.append((exit_time, tw))
        total_weight += tw
        last_load_time = load_time
        
    return bridge[-1][0]