def solution(sequence, k):
    INF = int(1e9)
    answer = [INF, INF]
    st, ed, cur = 0, 0, sequence[0]
    length = len(sequence)
    cur_length = INF
    # ed - st가 제일 짧은 거를 찾아서 하면 되는거잖아
    while st < length:
        if cur == k:
            if ed - st < cur_length:
                cur_length = ed - st
                answer = [st, ed]
            cur -= sequence[st]
            st += 1
        elif cur > k and st < length:
            cur -= sequence[st]
            st += 1
        elif ed + 1 < length:
            ed += 1
            cur += sequence[ed]
        else:
            break
    return answer