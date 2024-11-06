import heapq
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n)]
    INF = int(1e9)
    # cost는 무조건 1로
    for s, e in edge:
        graph[s-1].append((e-1, 1))
        graph[e-1].append((s-1,1))
    def dikstra(i):
        distances = [INF] * n
        q = []
        distances[i] = 0
        heapq.heappush(q, (0, i))
        while q:
            dis, now = heapq.heappop(q)
            if distances[now] < dis:
                continue
            for to, cost in graph[now]:
                dist = dis + cost
                if dist < distances[to]:
                    distances[to] = dist
                    heapq.heappush(q,(dist, to))
        return distances
    arr = dikstra(0)
    max_dis = 0
    for dis in arr:
        if dis > max_dis:
            answer = 1
            max_dis = dis
        elif dis == max_dis:
            answer += 1
    return answer