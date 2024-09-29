import sys
input = sys.stdin.readline
N, K = map(int, input().split())
# 이거 투 포인터인데..?
# 해가지고 겹치는 부분 해버려서 아니다 싶으면 줄이고
# 근데 겹치는 걸 어떻게 줄이지..? 그 보석도둑 때를 이용하자
arr = list(map(int, input().split()))
# 시작점, 끝점 , 중복갯수,  최장 길이
start = end = max_len = 0
# 겹침 관련 dict
dup_dict = {}
while start < len(arr):
    if len(arr) - start - 1 < max_len:
        break
    if end == len(arr):
        dup_dict[arr[start]] -= 1
        start += 1
    else:
        if not arr[end] in dup_dict:
            dup_dict[arr[end]] = 1
        else:
            dup_dict[arr[end]] += 1
        if end < len(arr) and arr[end] in dup_dict and dup_dict[arr[end]] > K:
            while dup_dict[arr[end]] > K:
                dup_dict[arr[start]] -= 1
                start += 1
        end += 1
    if end - start > max_len:
        max_len = end - start
print(max_len)
