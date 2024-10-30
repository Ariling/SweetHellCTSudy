import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(input().rstrip()))
check = [[False] * N for _ in range(N)]
weekCheck = [[False] * N for _ in range(N)]
normalColor = 0
weekColor = 0
def bfs(case, i, j, checkArr):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    q = deque([])
    q.append((i,j, arr[i][j]))
    checkArr[i][j] = True
    while q:
        r, c, color = q.popleft()
        for d in range(4):
            newR = r + dr[d]
            newC = c + dc[d]
            if 0 <= newR < N and 0 <= newC < N and not checkArr[newR][newC]:
                if case == 0 and arr[newR][newC] == color:
                    q.append((newR, newC, arr[newR][newC]))
                    checkArr[newR][newC] = True
                if case == 1:
                    if (color == 'B' and color == arr[newR][newC]) or ((color == 'R' or color == 'G') and (arr[newR][newC] == 'R' or arr[newR][newC] == 'G')):
                        q.append((newR, newC, arr[newR][newC]))
                        checkArr[newR][newC] = True
for i in range(N):
    for j in range(N):
        if not check[i][j]:
            bfs(0, i, j, check)
            normalColor += 1
        if not weekCheck[i][j]:
            bfs(1, i, j, weekCheck)
            weekColor += 1
print(normalColor, weekColor)