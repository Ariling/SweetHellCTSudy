import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())

graph = [[False] * (n+1) for _ in range(n+1)]

for i in range(m) :
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
    
dvisited = [False] * (n+1)
bvisited = [False] * (n+1)

def dfs(v):
    dvisited[v] = True
    print(v, end=" ")
    for i in range(1, n+1):
        if not dvisited[i] and graph[v][i] == 1:
            dfs(i)
            
def bfs(v):
    q = deque([v])
    bvisited[v] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if not bvisited[i] and graph[v][i] == 1:
                q.append(i)
                bvisited[i] = True
dfs(v)
print()
bfs(v)