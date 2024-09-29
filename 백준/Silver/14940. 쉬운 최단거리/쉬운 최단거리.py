import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = [[-1] * M for _ in range(N)]
endx = endy = 0
def bfs(x,y):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    q = deque([])
    check = [[False] * M for _ in range(N)]
    check[x][y] = True
    # start 지점은 0으로 해줘야지! 목표지점에서 목표지점은 0이니깐
    answer[x][y] = 0
    q.append((x, y))
    while q:
        r, c = q.popleft()
        for i in range(4):
            newR = r + dr[i]
            newC = c + dc[i]
            if 0 <= newR < N and 0 <= newC < M:
                if not check[newR][newC]:
                    if arr[newR][newC] == 1:
                        check[newR][newC] = True
                        answer[newR][newC] = answer[r][c] + 1
                        q.append((newR, newC))
                    elif arr[newR][newC] == 0:
                        continue

    return
# 이중 배열 탈출하는 법
# 그냥 벽 만나면 여기서 초기화해줘서 한번 continue로 넘겨보기
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 2:
            endx = i
            endy = j
        elif arr[i][j] == 0:
            answer[i][j] = 0
    else:
        continue
    break
bfs(endx, endy)
for r in answer:
    for c in r:
        print(c, end=' ')
    print()