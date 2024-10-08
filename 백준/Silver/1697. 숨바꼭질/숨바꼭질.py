import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
arr = [0] * 100001
check = [False] * 100001
q = deque([])
q.append((N, 0))
check[N] = True
while q:
    pos, time = q.popleft()
    arr[pos] = time
    if pos == K:
        break
    for i in (pos-1, pos+1, 2*pos):
        if 0 <= i <= 100000:
            if not check[i]:
                check[i] = True
                q.append((i, time + 1))
print(arr[K])