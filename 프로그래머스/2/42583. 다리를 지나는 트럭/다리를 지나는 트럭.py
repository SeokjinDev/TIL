from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge, trucks = deque([0]*bridge_length), deque(truck_weights)
    answer = 0
    while trucks:
        now = trucks[0]
        bridge.popleft()
        t = 1
        if sum(bridge) + now <= weight:
            bridge.append(trucks.popleft())
        else:
            while bridge[0] == 0:
                bridge.popleft()
                t += 1
            bridge.extend([0] * t)
        answer += t
    answer += bridge_length
    return answer