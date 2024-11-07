import sys
from collections import deque
input = sys.stdin.readline
dr = [-1, 1, 0, 0, -1, 1, -1, 1] # 좌상, 좌하, 우상, 우하
dc = [0, 0, -1, 1, -1, -1, 1, 1]
while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(H)]
    checked = [[False] * W for _ in range(H)]
    land = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 1 and not checked[i][j]:
                q = deque([])
                q.append((i, j))
                checked[i][j] = True
                while q:
                    r, c = q.popleft()
                    for k in range(8):
                        newR = r + dr[k]
                        newC = c + dc[k]
                        if 0 <= newR < H and 0 <= newC < W:
                            if arr[newR][newC] == 1 and not checked[newR][newC]:
                                q.append((newR, newC))
                                checked[newR][newC] = True
                land += 1
    print(land)
