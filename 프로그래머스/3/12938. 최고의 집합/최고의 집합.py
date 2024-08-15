def solution(n, s):
    answer = []
    # n이 3일때 가정하면 (2,7) * 3 이냐 (2,6) * 4 이거 결국 3,3,4야.. 
    # 그러고 n이 2일때 그러면 8일때를 고려하면 (1,4) * 4 이런걸 다 고려해서 해야되고...
    # 잠만 가운데 숫자가 제일 크잖아... 그러면 1일때를 제외하면... 2일때는... 맞고
    # -1인 경우가 또 있나..? 3일때 안되는거 3보다 작으면 안되는 거잖아 -> 테케를 고려안했네
    if n == 1:
        return [s]
    elif s // n == 0:
        return [-1]
    else:
        for i in range(n):
            answer.append(s // n)
        for i in range(1,(s%n)+1):
            answer[-i] += 1
        return answer