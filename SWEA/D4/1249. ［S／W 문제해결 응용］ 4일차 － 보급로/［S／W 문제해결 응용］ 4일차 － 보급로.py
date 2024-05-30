from collections import *

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(arr, visited, time, start, end):
    deq = deque([start])
    while deq:
        x, y = deq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if nx == 0 and ny == 0: continue
                elif visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    time[nx][ny] = time[x][y] + arr[nx][ny]
                    deq.append((nx, ny))
                else:
                    if time[nx][ny] > time[x][y] + arr[nx][ny]:
                        time[nx][ny] = time[x][y] + arr[nx][ny]
                        deq.append((nx, ny))



for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(list(map(int, input())) for _ in range(N)) # 이렇게 배열 만들기.. 

    visited = [[0] * N for _ in range(N)]
    time = [[0] * N for _ in range(N)]
    start , end = [0, 0], [N - 1, N - 1]
    
    bfs(arr, visited, time, start, end)
    answer = time[end[0]][end[1]]
    
    print(f'#{tc} {answer}') # 이렇게 print하기 