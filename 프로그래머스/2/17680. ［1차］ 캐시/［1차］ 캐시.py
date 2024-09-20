from collections import deque
def solution(cacheSize, cities):
    # 캐시크기와 도시이름 배열을 받았어..
    # 그런 다음에..?
    # hit이면 1이고 miss면 5라고?
    # 아아아 이해했어, LRU 란 맨 앞에 넣고 해당하는게 있으면 그걸 빼고 다시 맨 앞에 넣는 형식
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    cache_arr = [" "] * cacheSize
    for city in cities:
        # 대 소문자
        city = city.lower()
        if not city in cache_arr:
            cache_arr.pop()
            cache_arr.insert(0, city)
            answer += 5
        else:
            idx = cache_arr.index(city)
            cache_arr.pop(idx)
            cache_arr.insert(0, city)
            answer += 1
    return answer