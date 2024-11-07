import sys
import heapq
input = sys.stdin.readline

T = int(input())
arr = []
for _ in range(T):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x:(x[0], x[1]))
heap = [(arr[0][1], arr[0][0])] # 아 끝나는 시간으로 하라고..?
for i in range(1, T):
    if arr[i][0] >= heap[0][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, (arr[i][1], arr[i][0]))
print(len(heap))