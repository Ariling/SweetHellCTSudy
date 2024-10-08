import sys
from collections import deque
input = sys.stdin.readline
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
def bfs(x,y, check):
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    q= deque([])
    q.append((x,y))
    check[x][y] = True
    union = deque([])
    total = 0
    while q:
        r, c = q.popleft()
        total += arr[r][c]
        union.append((r,c))
        for i in range(4):
            newR = r + dr[i]
            newC = c + dc[i]
            if 0 <= newR < N and 0 <= newC < N:
                if not check[newR][newC] and L <= abs(arr[r][c] - arr[newR][newC]) <= R:
                    q.append((newR, newC))
                    check[newR][newC] = True
    if len(union) > 1:
        change_num = total // len(union)
        for r,c in union:
            arr[r][c] = change_num
        return True
    return False
while True:
    check = [[False] * N for _ in range(N)]
    finish = False
    # 아하? 각각 해줘야 하는구나! 그리고 각각 union 찾는 과정은 check를 넘겨주면 된다!
    for i in range(N):
        for j in range(N):
            if not check[i][j]:
                if bfs(i, j, check):
                    finish = True
    if not finish:
        break
    result += 1
print(result)
