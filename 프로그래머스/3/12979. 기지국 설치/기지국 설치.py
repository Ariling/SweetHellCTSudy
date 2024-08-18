import math
def solution(n, stations, w):
    answer = 0
    coverage = 2 * w + 1
    start = 1
    # 이거 greedy인 것 같고..
    # 마음편히 1번 인덱스부터 출발을 해버리고 +-W를 해버린 1을 해버리고..
    # 1인 경우는 무조건 건너뛰고 0이면 그 확인을 해서 허어... 근데 어떻게 해야되지..? 이게 관건이네
    # 이거 설치하냐 안하냐가 문제네...
    for station in stations:
        end = station - w
        if end > start:
            answer += math.ceil((end - start) / coverage)
        start = station + w + 1
    
    if start <= n:
        answer += math.ceil((n - start + 1) / coverage)
    
    return answer