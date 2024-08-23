import heapq
def solution(book_time):
    # 분 형태로 바꾸고 나서 정렬을 한 뒤, 그거 end 타임 정해두고 하면 되는 거 아닌가?
    book_time_array = []
    for start, end in book_time:
        start_time = (int(start[:2]) * 60) + int(start[3:])
        end_time = (int(end[:2]) * 60) + int(end[3:]) 
        book_time_array.append([start_time, end_time])
    book_time_array = sorted(book_time_array, key=lambda x : (x[0], x[1]))
    room = []
    for start, end in book_time_array:
        if room and start >= room[0]:
            heapq.heappop(room)
        heapq.heappush(room, end+10)
    return len(room)