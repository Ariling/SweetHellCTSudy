import sys
input = sys.stdin.readline
# 재귀 제한을 넓혀야 한대..
sys.setrecursionlimit(5000)
# 이거 정점이랑 간선이래..
N, M = map(int, input().split())
graph = [[0] * N for _ in range(N)]
visited = [False] * N
for _ in range(M):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1
connect = 0
def dfs(i):
    visited[i] = True
    for j in range(N):
        if graph[i][j] == 1 and not visited[j]:
            visited[j] = True
            dfs(j)

for i in range(N):
    if not visited[i]:
        dfs(i)
        connect += 1
print(connect)