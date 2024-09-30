import sys
import heapq
input = sys.stdin.readline
N , M = map(int, input().split())
INF = int(1e9)
# 근데 이거 안 터지나? 당장 생각나는 건 다익스트라 뿐인데..?
graph = [[0] * N for _ in range(N)]
result = INF
resultIdx = -1
for _ in range(M):
    s, e = map(int, input().split())
    graph[s-1][e-1] = 1
    graph[e-1][s-1] = 1
def dikstra(i):
    distances = [INF] * N
    q = []
    heapq.heappush(q,(0, i))
    distances[i] = 0
    while q:
        dis, now = heapq.heappop(q)
        if distances[now] < dis:
            continue
        for to in range(N):
            if graph[now][to] == 0:
                continue
            dist = dis + graph[now][to]
            if dist < distances[to]:
                distances[to] = dist
                heapq.heappush(q,(dist, to))
    return sum(distances)
for i in range(N):
    kevin = dikstra(i)
    if kevin < result:
        result = kevin
        resultIdx = i
print(resultIdx+1)