def solution(gems):
    # 먼저 보석 종류 구하기
    # 사전으로 담고 사전에 있는 가장 작은 갯수가 1일때 return을 해버리기
    gems_set = set(gems)
    gems_dict = {}
    length = 1e9
    start = 0
    end = 0
    answer = []
    for i in range(len(gems)):
        if not gems[i] in gems_dict:
            gems_dict[gems[i]] = 0
        gems_dict[gems[i]] += 1
        while gems_dict[gems[start]] > 1:
            gems_dict[gems[start]] -= 1
            start += 1
        if len(gems_dict) == len(gems_set) and length > i - start:
            length = i - start
            answer = [start + 1, i + 1]
    return answer