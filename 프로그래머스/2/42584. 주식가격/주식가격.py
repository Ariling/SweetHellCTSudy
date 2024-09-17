def solution(prices):
    # 이거 스택이고... 내가 봤을때 idx에 따라와 stack의 길이에 따라서 장난 치는 것 같아.. 이거 말고는 말이 안되.
    
    answer = [0 for _ in range(len(prices))]
    stack = []
    for i in range(len(prices)):
        time = 0
        for j in range(i+1, len(prices)):
            time += 1
            if prices[i] > prices[j]:
                break
        answer[i] = time
    return answer