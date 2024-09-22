import heapq
def solution(n, results):
    # 1번부터 n번까지 번호를 받았다. 실력이 좋으면 항상 이긴다.
    # 정확하게 순위를 매길 수 있는 선수의 수
    # 아 잠만.... A선수가 B를 이겼다라는 뜻이 [A, B] 이기면 2 졌으면 1 이런식으로 넣어야겠다.. 그러면
    answer = 0
    graph = [[0] * n for _ in range(n)]
    graph_cnt = [0] * n
    # 어떻게 유추를 할 수 있는... 그거를 만들 수 있을까?
    for A, B in results:
        graph[A-1][B-1] = 2
        graph[B-1][A-1] = 1
    for k in range(n):
        for a in range(n):
            for b in range(n):
                # 약간 그거네? 명제 문제 같이 푸는거?
                # graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) -> 원래는 그냥 이건데?
                if graph[a][k] == 2 and graph[k][b] == 2:
                    graph[a][b] = 2
                elif graph[a][k] == 1 and graph[k][b] == 1:
                    graph[a][b] = 1
    for r in graph:
        cnt = 0
        for c in r:
            if c != 0:
                cnt += 1
        if cnt == n-1:
            answer += 1
    return answer