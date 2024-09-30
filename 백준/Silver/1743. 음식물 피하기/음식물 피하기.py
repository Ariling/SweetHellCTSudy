import sys
from collections import deque
input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
check = [[False] * M for _ in range(N)]
result = 0
for _ in range(K):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def bfs(i, j):
    q = deque([])
    q.append((i, j))
    count = 1
    check[i][j] = True
    while q:
        r, c = q.popleft()
        for idx in range(4):
            newR = r + dr[idx]
            newC = c + dc[idx]
            if 0 <= newR < N and 0<= newC < M:
                if arr[newR][newC] == 1 and not check[newR][newC]:
                    q.append((newR, newC))
                    check[newR][newC] = True
                    count += 1
    return count
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and not check[i][j]:
            num = bfs(i, j)
            if num > result:
                result = num
print(result)