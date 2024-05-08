def solution(bridge_length, weight, truck_weights):
    answer = 0
    if bridge_length == 1 : return len(truck_weights)+1;
    if len(truck_weights) == 1: return bridge_length + 1;
    index = 0
    sum = 0
    q = list()
    for i in range(bridge_length):
       q.append(0)
    while index < len(truck_weights):
        sum -= q.pop(0)
        answer += 1
        if sum+truck_weights[index] <= weight:
            sum += truck_weights[index]
            q.append(truck_weights[index])
            index += 1
        else:
            q.append(0)
    return answer+bridge_length