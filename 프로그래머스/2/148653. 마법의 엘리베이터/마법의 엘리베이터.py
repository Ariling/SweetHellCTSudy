def solution(storey):
    answer = 0
    btn = 1
    # 이거 자릿수만 나누는 방법! map을 잘 쓰자.. 백준때도 그랬지만
    num_list = list(map(int, reversed(str(storey))))
    i = 0
    while i < len(num_list):
        if num_list[i] > 5:
            if i == len(num_list) - 1:
                answer += (11 - num_list[i])
            else:
                num_list[i + 1] += 1
                answer += (10 - num_list[i])
        elif num_list[i] == 5:
            if i == len(num_list) - 1:
                answer += (10 - num_list[i])
            else:
                if num_list[i + 1] >= 5:
                    num_list[i + 1] += 1
                    answer += (10 - num_list[i])
                else:
                    answer += num_list[i]
        else:
            answer += num_list[i]
        i += 1
        btn *= 10
    return answer