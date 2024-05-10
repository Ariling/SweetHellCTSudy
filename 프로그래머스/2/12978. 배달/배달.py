import heapq
# 이게 큰 수를 만드는 방법
INF = 1e8
def solution(N, road, K):
    answer = 0
    # 1번부터 출발한다고 하기 때문에 이를 적으면 된다.
    # 음수로 해두면 일단 아닌게 확실하기 때문
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)
    # 이거 양방향 처리해야되네...
    for i in range(len(road)):
        graph[road[i][0]].append((road[i][1], road[i][2]))
        graph[road[i][1]].append((road[i][0], road[i][2]))
    dijkstra(1, distance, graph)
    for num in distance:
        if num <= K:
            answer += 1
    return answer

# 이건 좀 참고해서 만들었음...
def dijkstra(start, distance, graph):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            if dist+i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist+i[1], i[0]))