import sys
from collections import deque
input = sys.stdin.readline

# 3차원은 오바다.. 만약 나오면 운명이려니 해..
C, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
q = deque([])
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for i in range(R):
    for j in range(C):
        if arr[i][j] == 1:
            q.append((i, j))
def bfs():
    while q:
        i, j = q.popleft()
        for k in range(4):
            r = i + dr[k]
            c = j + dc[k]
            if 0 <= r < R and 0 <= c < C:
                if arr[r][c] == 0:
                    arr[r][c] = arr[i][j] + 1 # 이거를 해줘야 하는게 그래야 날이 지난 걸 알 수 있음
                    q.append((r, c))
bfs()
isNotComplete = False
day = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == 0:
            isNotComplete = True
            break
        day = max(day, arr[i][j])
if isNotComplete:
    print(-1)
else:
    print(day-1)