import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 존재하는 높잇값들만 집합으로 저장하기
arr_max_value = set(sum(arr, []))
result = 1
dr = [-1, 1, 0, 0]
dc = [0,0,-1,1]
for n in arr_max_value:
    check = [[False] * N for _ in range(N)]
    q = deque([])
    land_cnt = 0
    for i in range(N):
        for j in range(N):
            if check[i][j] or arr[i][j] <= n:
                continue
            land_cnt += 1
            check[i][j] = True
            q.append((i, j))
            while q:
                r, c = q.popleft()
                for d in range(4):
                    newR = r + dr[d]
                    newC = c + dc[d]
                    if 0 <= newR < N and 0 <= newC < N and not check[newR][newC] and arr[newR][newC] > n:
                        q.append((newR, newC))
                        check[newR][newC] = True
    result = max(result, land_cnt)
print(result)
