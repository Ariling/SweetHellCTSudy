import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for _ in range(T):
    answer = 0
    M, N, K = map(int, input().split())
    arr = [[0] * N for _ in range(M)]
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[X][Y] = 1
    q = deque([])
    check = [[False] * N for _ in range(M)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1 and not check[i][j]:
                q.append((i, j))
                check[i][j] = True
                while q:
                    r, c = q.popleft()
                    for idx in range(4):
                        newR = r + dr[idx]
                        newC = c + dc[idx]
                        if 0 <= newR < M and 0 <= newC < N:
                            if arr[newR][newC] == 1 and not check[newR][newC]:
                                check[newR][newC] = True
                                q.append((newR, newC))
                answer += 1
    print(answer)