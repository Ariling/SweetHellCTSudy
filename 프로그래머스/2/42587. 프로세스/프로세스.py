from collections import deque
def solution(priorities, location):
    # 우선순위 num이높을 수록 먼저 처리 몇 번째로 처리가 되는지?
    # 우선 순위 처리.. 이거 헷갈리네? 이거는 그 q를 따로 넣어야 겠다.
    q = deque([i for i in range(len(priorities))])
    priorities = deque(priorities)
    answer = 0
    while location in q:
        maxp = max(priorities)
        print(maxp)
        while priorities[0] != maxp:
            num = priorities.popleft()
            priorities.append(num)
            position = q.popleft()
            q.append(position)
        priorities.popleft()
        q.popleft()
        answer += 1
    return answer