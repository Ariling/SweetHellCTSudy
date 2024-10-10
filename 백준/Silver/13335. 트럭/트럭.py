import sys
from collections import deque
input = sys.stdin.readline
# 갯수, 길이, 무게
N, W, L = map(int, input().split())
arr = list(map(int, input().split()))
q = deque([0] * W)
cnt = 0
while q:
    q.popleft()
    cnt += 1
    if not arr:
        continue
    if sum(q) + arr[0] <= L:
        q.append(arr[0])
        arr.remove(arr[0])
    else:
        q.append(0)
print(cnt)