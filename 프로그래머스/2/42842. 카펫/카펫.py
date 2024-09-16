import math
def solution(brown, yellow):
    answer = []
    # 잠만 이거 답은 그러면 그거네..? 그 옐로우 길이의 각각 2씩 더한거?
    if yellow == 1:
        return [3, 3]
    else:
        list = [i+1 for i in range(int(math.sqrt(yellow) // 1))]
        for c in list:
            if yellow % c == 0:
                r = yellow // c
                if (2*(r+2)) + (2*c) == brown:
                    return [r + 2, c + 2]
    return answer