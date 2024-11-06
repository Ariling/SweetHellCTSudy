import sys
import heapq
input = sys.stdin.readline
N = int(input())
V = int(input())
graph = [[] for _ in range(N)]
INF = int(1e9)
for _ in range(V):
    s, e = map(int, input().split())
    graph[s-1].append((e-1, 1))
    graph[e-1].append((s-1, 1))
def dikstra(i):
    distances = [INF] * N
    q = []
    distances[i] = 0
    heapq.heappush(q, (0, i))
    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for to, cost in graph[now]:
            distance = dist + cost
            if distance < distances[to]:
                distances[to] = distance
                heapq.heappush(q,(distance, to))
    return distances
arr = dikstra(0)
answer = 0
for i in range(1, len(arr)):
    # 극단적인 경우에는 N까지가 끝이기 때문
    if arr[i] < N:
        answer += 1
print(answer)