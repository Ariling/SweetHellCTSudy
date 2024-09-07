import heapq
def solution(n, costs):
    graph = [[0] * n for _ in range(n)]
    for cost in costs:
        graph[cost[0]][cost[1]] = cost[2]
        graph[cost[1]][cost[0]] = cost[2]
    # 이거 그거 아냐..? 그래프... 그리고 그 MST 방식
    pq = []
    # 이렇게 체크를 해야함 거의 bfs랑 비슷한 방식
    visited = [False] * n
    min_weight = 0
    edge_count = 0
    heapq.heappush(pq,(0, 0))
    while pq and edge_count < n:
        weight, now = heapq.heappop(pq)
        if visited[now]:
            continue
        visited[now] = True
        min_weight += weight
        edge_count += 1
        for to in range(n):
            if graph[now][to] > 0 and not visited[to]:
                heapq.heappush(pq, (graph[now][to], to))
    return min_weight