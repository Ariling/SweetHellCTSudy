def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        # 이렇게 간단하게 만들면 되는구나
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer