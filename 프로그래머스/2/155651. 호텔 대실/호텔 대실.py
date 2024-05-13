import heapq
def solution(book_time):
    time_arr = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s,e in book_time]
    time_arr.sort()
    heap = []
    for i in time_arr:
        if len(heap) != 0 and i[0] >= heap[0]+10:
            heapq.heappop(heap)
        heapq.heappush(heap, i[1])
    answer = len(heap)
    return answer