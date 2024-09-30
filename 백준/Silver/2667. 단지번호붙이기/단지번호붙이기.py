import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
# 공백으로 주면 split 아니면 strip으로 처리하기!
# 치즈도둑 같은거지
arr = [list(map(int, input().strip())) for _ in range(N)]
check = [[False] * N for _ in range(N)]
result_arr = []
def bfs(i, j):
    q = deque([])
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    q.append((i,j))
    check[i][j] = True
    num = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            newR = r + dr[i]
            newC = c + dc[i]
            if 0 <= newR < N and 0 <= newC < N:
                if not check[newR][newC] and arr[newR][newC] == 1:
                    check[newR][newC] = True
                    q.append((newR, newC))
                    num += 1
    return num
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if not check[i][j] and arr[i][j] == 1:
            num = bfs(i, j)
            result_arr.append(num)
result_arr = sorted(result_arr)
print(len(result_arr))
for num in result_arr:
    print(num)