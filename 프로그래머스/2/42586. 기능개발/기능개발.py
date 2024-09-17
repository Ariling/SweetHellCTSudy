from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    finish = deque([])
    for i in range(len(speeds)):
        finish_time = math.ceil((100 - progresses[i]) / speeds[i])
        finish.append(finish_time)
    # 걍 여기서부터 출발시키자
    time = finish.popleft()
    cnt = 1
    while finish:
        if time < finish[0]:
            answer.append(cnt)
            time = finish.popleft()
            cnt = 1
        else:
            finish.popleft()
            cnt += 1
    # 마지막은 스스로 추가를 해야 한다.
    answer.append(cnt)
    return answer