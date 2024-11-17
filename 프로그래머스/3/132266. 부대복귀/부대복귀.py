import heapq
def solution(n, roads, sources, destination):
    #n 총 지역의 수
    # 두 지역을 왕복할 수 있는 길
    # 각 부대원이 위치한 서로 다른 지역들을 나타내는 게 sources
    # 강철부대 지역이 destination
    # 주어진 sources원소 순서대로 강철부대로 복귀할 수 있는 최단시간을 담는 배열 return
    # 아! 그 sources마다 그 돌아갈 수 있는 길을 정해야 하는구나.. 
    # 이거 그러면 그냥... 그 그래프 문제로 해결할 수 있는거 아닌가..?
    answer = []
    graph = [[] for _ in range(n+1)]
    for road in roads:
        graph[road[0]].append((road[1],1))
        graph[road[1]].append((road[0],1))
    INF = int(1e9)
    def dikstra(i):
        distances = [INF] * (n+1)
        distances[0] = -1
        q = []
        distances[i] = 0
        heapq.heappush(q,(0, i))
        while q:
            dis, now = heapq.heappop(q)
            if dis > distances[now]:
                continue
            for to, cost in graph[now]:
                dist = dis + cost
                if dist < distances[to]:
                    distances[to] = dist
                    heapq.heappush(q,(dist, to))
        return distances
    desti_arr = dikstra(destination)
    for source in sources:
        if desti_arr[source] > n:
            answer.append(-1)
        else:
            answer.append(desti_arr[source])
    return answer