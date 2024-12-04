from collections import deque
def solution(picks, minerals):
    INF = int(1e9)
    answer = INF
    arr = [minerals[i:i+5] for i in range(0, len(minerals), 5)]
    def get_piro(pick_type, i):
        piro = 0
        mineral_arr = arr[i][:]
        while mineral_arr:
            mineral = mineral_arr.pop()
            if pick_type == 0:
                piro += 1
            elif pick_type == 1:
                if mineral == 'diamond':
                    piro += 5
                else:
                    piro += 1
            else:
                if mineral == 'diamond':
                    piro += 25
                elif mineral == 'iron':
                    piro += 5
                else:
                    piro += 1
        return piro
                
            
    def search_mineral(i, tem_picks, piro):
        nonlocal answer
        if i == len(arr) or sum(tem_picks) == 0:
            if piro < answer:
                answer = piro
            return
        if piro >= answer:
            return
        for pick_type in range(3):
            if tem_picks[pick_type] > 0:
                # 이게 복사하는 방법
                new_picks = tem_picks[:]
                new_picks[pick_type] -= 1
                new_piro = piro + get_piro(pick_type, i)
                search_mineral(i+1, new_picks, new_piro)
    search_mineral(0, picks, 0)
    return answer