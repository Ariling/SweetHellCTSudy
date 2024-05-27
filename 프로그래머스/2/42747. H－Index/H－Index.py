def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)+1):
        h_index = 0
        for num in citations:
            if num >= i:
                h_index += 1
        if i > h_index:
            answer = i - 1
            break
        else:
            answer = i
    return answer