def solution(n, k, enemy):
    # 이거 완탐인가..? 딱 봤을 때 idx 0부터 시작을 해서 defense를 쓰냐 안 쓰냐에 따라서 구하고..
    # 이거 그 idx max로 answer를 해서 결국 끝은 그냥 answer+1을 return하면 되는 거 아닌가?
    answer = 0
    # def search(idx, defense, rest):
    #     nonlocal answer
    #     # 끝나는 조건, 끝에 도달했거나 살아남은 애들이 없거나 그럴때
    #     if idx == len(enemy): 
    #         answer = max(answer, idx)
    #         return
    #     if rest >= enemy[idx]:
    #         search(idx + 1, defense, rest - enemy[idx])
    #     if defense > 0:
    #         search(idx + 1, defense - 1, rest)
    #     if rest - enemy[idx] < 0 and defense == 0:
    #         answer = max(answer, idx)
    #         return
    # search(0, k, n)
    left, right = 0, len(enemy) - 1
    def clear(mid, cnt):
        # 이 아이들까지 sort를 하는거야....
        sort_enemy = sorted(enemy[:mid+1])
        rest = n
        defense = k
        for num in sort_enemy:
            if rest - num < 0:
                break
            else:
                rest = rest - num
                cnt += 1
        if mid - cnt < defense:
            return True
        else:
            return False
    while left <= right:
        mid = (left + right) // 2
        possible = clear(mid, 0)
        if possible:
            left = mid + 1
        else:
            right = mid - 1
            answer = right
    answer = right
    return answer+1