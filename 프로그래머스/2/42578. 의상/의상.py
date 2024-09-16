def solution(clothes):
    answer = 1
    cloth_collect = {}
    for cloth in clothes:
        if not cloth[1] in cloth_collect:
            cloth_collect[cloth[1]] = []
        cloth_collect[cloth[1]].append(cloth[0])
    # 얠 분류하는 건 성공했는데 여기서 어떻게 조합을 맞추냐...
    key_list = cloth_collect.keys()
    for key in key_list:
        answer *= len(cloth_collect[key])+1
    answer -= 1
    return answer