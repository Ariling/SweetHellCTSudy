import heapq
def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    graph = [[0] * N for _ in range(N)]
    for s, e, time in road:
        if graph[s-1][e-1] != 0 and graph[s-1][e-1] <= time:
            continue
        # 할당하기 위한 방법, idx는 0부터니깐 그거에 맞춰서!
        graph[s-1][e-1] = time
        graph[e-1][s-1] = time
    # 시작점부터 나타내주는 다익스트라 함수 만들기 (배열이나 q등 다 여기에 넣고 한다.)
    def dikstra(start):
        distances = [INF] * N
        q = []
        # 시간, 지점 순으로 넣기
        heapq.heappush(q,(0, start))
        distances[start] = 0
        while q:
            time, now = heapq.heappop(q)
            # 현재 가지고 있는 거리가 시간 보다 작다면 굳이 할 필요가 없음
            if distances[now] < time:
                continue
            # 도착 지점을 정할 때는 연결지점을 반드시 확인해보기
            for to in range(N):
                # 0이면 굳이 밑에 있는 애들을 할 필요가 없다.
                if graph[to][now] == 0:
                    continue
                # 거리 구하는 공식 및 비교 방식
                dist = time + graph[to][now]
                if dist < distances[to]:
                    distances[to] = dist
                    heapq.heappush(q,(dist, to))
        return distances
    dist_arr = dikstra(0)
    for dist in dist_arr:
        if dist <= K:
            answer += 1
    return answer