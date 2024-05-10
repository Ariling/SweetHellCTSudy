from collections import defaultdict
def solution(tickets):
    tickets.sort()
    map = defaultdict(list)
    # 오... 이런식으로 하면 되는 구나?
    for depart, arrive in tickets:
        map[depart].append(arrive)
    stack, path = ["ICN"], []

    while stack:
        if map.get(stack[-1]):
            stack.append(map.get(stack[-1]).pop(0))
        else:
            path.append(stack.pop())
    
    # 와... 이렇게 하면 거꾸로가 되? 대박이네...
    answer = path[::-1]
    return answer