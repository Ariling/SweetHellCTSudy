import sys
from collections import deque
input = sys.stdin.readline

C, R = map(int, input().split())
arr = []
for _ in range(R):
    arr.append(list(map(int, input().rstrip())))
INF = int(1e9)
dis = [[INF] * C for _ in range(R)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    q = deque([])
    dis[r][c] = 0
    q.append((r, c, 0)) # 코스트까지 포함 할 것
    while q:
        x, y, cost = q.popleft()
        for i in range(4):
            newX = x + dr[i]
            newY = y + dc[i]
            if 0 <= newX < R and 0 <= newY < C:
                if dis[x][y] + arr[newX][newY] < dis[newX][newY]:
                    dis[newX][newY] = dis[x][y] + arr[newX][newY]
                    q.append((newX, newY, dis[newX][newY]))
bfs(0, 0)
print(dis[R-1][C-1])