import sys
import heapq
input = sys.stdin.readline
N , V = map(int, input().split())
# 아... 거리가 0부터 시작이냐 1부터 시작이냐를 잘 봐야하네
# 인접행렬은 메모리 초과가 일어날 가능성이 있으니 인접리스트를 활용하래..
graph = [[] for _ in range(N)]
# graph = [[-1] * N for _ in range(N)]
INF = int(1e9)
for _ in range(V):
    s, e, c = map(int, input().split())
    graph[s-1].append((e-1, c))
    graph[e-1].append((s-1, c))
    # if graph[s-1][e-1] != -1 and graph[s-1][e-1] <= c:
    #     continue
    # graph[s-1][e-1] = c
    # graph[e-1][s-1] = c
def dikstra(i):
    distances = [INF] * N
    q = []
    distances[i] = 0
    heapq.heappush(q,(0, i))
    while q:
        dis, now = heapq.heappop(q)
        if distances[now] < dis:
            continue
        # 여기에 Cost가 더 한 것
        # for to in range(N):
        for to, cost in graph[now]:
            # if graph[now][to] == -1:
            #     continue
            dist = dis + cost
            if dist < distances[to]:
                distances[to] = dist
                heapq.heappush(q, (dist, to))
    return distances
arr = dikstra(0)
print(arr[N-1])