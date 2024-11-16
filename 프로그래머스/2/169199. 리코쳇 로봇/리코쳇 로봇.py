from collections import deque
def solution(board):
    INF = int(1e9)
    answer = INF
    arr = []
    for string in board:
        arr.append([*string])
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    boardR = len(arr)
    boardC = len(arr[0])
    isFind = False
    redX = 0
    redY = 0
    for i in range(boardR):
        for j in range(boardC):
            if arr[i][j] == 'R':
                redX = i
                redY = j
                break
    def bfs(x,y):
        nonlocal answer, isFind
        q = deque([])
        q.append((x,y, 0))
        distance = [[INF] * boardC for _ in range(boardR)]
        distance[x][y] = 0
        while q:
            r, c, dis = q.popleft()
            if arr[r][c] == 'G':
                isFind = True
                answer = min(answer, dis)
                continue
            if arr[r][c] != 'G' and dis >= answer:
                continue
            else:
                for i in range(4):
                    newR = r + dr[i]
                    newC = c + dc[i]
                    if newR < 0 or newR >= boardR or newC < 0 or newC >= boardC:
                        continue
                    else:
                        while 0 <= newR < boardR and 0 <= newC < boardC:
                            if arr[newR][newC] == 'D':
                                break
                            else:
                                newR += dr[i]
                                newC += dc[i]
                        newR -= dr[i]
                        newC -= dc[i]
                        if dis + 1 < distance[newR][newC]: 
                            distance[newR][newC] = dis + 1
                            q.appendleft((newR, newC, dis+1))
    bfs(redX, redY)
    if not isFind:
        answer = -1
    return answer