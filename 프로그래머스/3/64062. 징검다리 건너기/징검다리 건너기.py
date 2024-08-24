def solution(stones, k):
    answer = 0
    min_stone = min(stones)
    max_stone = max(stones)
    def walk(mid, cnt, stones):
        for stone in stones:
            if stone < mid:
                cnt += 1
            else:
                cnt = 0
            if cnt == k:
                return False
        return True
    while min_stone < max_stone:
        mid_stone = (min_stone + max_stone + 1) // 2
        check = walk(mid_stone, 0, stones)
        # 중간값이 실제 stone들보다 큰 거니깐 min을 늘리는 방식인건가..?
        if check:
            min_stone = mid_stone
        # 중간값이 실제 stone들보다 작은거니깐 max를 늘리는 형태고
        else:
            max_stone = mid_stone - 1
    return max_stone