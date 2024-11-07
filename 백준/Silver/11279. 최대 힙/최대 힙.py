import sys
import heapq
input = sys.stdin.readline
N = int(input())
heap = []
for _ in range(N):
    case = int(input())
    if case == 0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        # 최대힙 할때는 이런식으로 해야 한다. 그래야 꺼낼 때 정상적으로 된다.
        heapq.heappush(heap, -case)