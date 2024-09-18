def solution(n, times):
    # 이분탐색이라는거는 left right를 두고...
    # left가 넘어갔을 때 멈추는 거잖아?
    # 이게 왜 이분탐색일까..?
    left, right = 1, min(times) * n
    answer = 0
    while left <= right:
        mid = (left+right)//2
        # left 는 mid + 1
        # right 는 mid - 1
        cnt = 0
        for time in times:
            cnt += mid // time
        if cnt < n:
            left = mid + 1
        else:
            # 더 담을 수 없을 때는 이렇게 하는 거네 
            right = mid - 1
            answer = mid
    return answer