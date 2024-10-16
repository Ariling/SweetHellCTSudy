import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]
house = []
chicken = []
INF = int(1e9)
result = INF
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append((i, j))
        elif arr[i][j] == 1:
            house.append((i, j))
for combi in combinations(chicken, M):
    dist = 0
    for h in house:
        house_dist = INF
        for c in combi:
            house_dist = min(house_dist, abs(h[1] - c[1]) + abs(h[0] - c[0]))
        dist += house_dist
    result = min(result, dist)
print(result)
