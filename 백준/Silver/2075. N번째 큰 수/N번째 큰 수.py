import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    plus_arr = list(map(int, input().split()))
    for i in range(len(plus_arr)):
        if len(arr) < N:
            heapq.heappush(arr, plus_arr[i])
        elif len(arr) == N and arr[0] < plus_arr[i]:
            heapq.heappop(arr)
            heapq.heappush(arr, plus_arr[i])
print(arr[0])