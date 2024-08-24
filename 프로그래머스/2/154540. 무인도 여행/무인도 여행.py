from collections import deque
def solution(maps):
    # 이거 그거 활용이다. bfs!
    maps_arr = [list(map_item) for map_item in maps]
    check = [[False for _ in range(len(maps_arr[0]))] for _ in range(len(maps_arr))]
    answer = []
    dr = [-1, 1, 0, 0] # 위 아래 왼 우
    dc = [0 , 0, -1, 1] 
    def bfs(r, c):
        q = deque([])
        land_scape = 0
        q.append((r, c))
        check[r][c] = True
        land_scape += int(maps_arr[r][c])
        while q:
            start_r, start_c = q.popleft()
            for i in range(4):
                new_r, new_c = start_r + dr[i], start_c + dc[i]
                if new_r < 0 or new_r >= len(maps_arr) or new_c < 0 or new_c >= len(maps_arr[0]):
                    continue
                if check[new_r][new_c] or maps_arr[new_r][new_c] == 'X':
                    continue
                else:
                    check[new_r][new_c] = True
                    q.append((new_r, new_c))
                    land_scape += int(maps_arr[new_r][new_c])
        return land_scape
    for i in range(len(maps_arr)):
        for j in range(len(maps_arr[i])):
            if not maps_arr[i][j] == 'X' and not check[i][j]:
                land = bfs(i, j)
                answer.append(land)
    if len(answer) == 0:
        return [-1]
    else:
        answer = sorted(answer)
        return answer