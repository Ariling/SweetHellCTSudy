def solution(sequence, k):
    # 이거 투 포인터 이용해서 하면 될 것 같은데...
    # start랑 end포인트 설정해가지고...
    # 이거 무조건 있는거지..?
    # 0부터 시작해서 end가 len(sequence)까지 가면 끝나는 걸로... start도 그래야 하나?
    # min_cnt 로 하고 startIdx, endIdx 설정해서 하는 걸로... 
    start, end, total = 0, 0, 0
    min_cnt = 1e9
    startIdx, endIdx = 1e9, 0
    while start < len(sequence):
        if total > k or end == len(sequence):
            total -= sequence[start]
            start += 1
        elif total <= k and end < len(sequence):
            total += sequence[end]
            end += 1
        if total == k and (end - start < min_cnt or (end - start == min_cnt and start < startIdx)):
            min_cnt = end - start
            startIdx = start
            endIdx = end
    answer = [startIdx, endIdx-1]
    return answer