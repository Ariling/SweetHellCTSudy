from collections import deque
def solution(maps):
    map_arr = [list(map_item) for map_item in maps]
    map_distance = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    # 시작점
    # 레버점
    # 종료점
    start_pos, l_pos, end_pos = [], [], []
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    def bfs(x, y, target):
        check = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
        q = deque()
        q.append((x,y))
        check[x][y] = True
        while q:
            r, c = q.popleft()
            if maps[r][c] == target:
                return map_distance[r][c]
            for i in range(4):
                new_r = r + dr[i]
                new_c = c + dc[i]
                if new_r < 0 or new_c < 0 or new_c >= len(map_arr[0]) or new_r >= len(map_arr):
                    continue
                if maps[new_r][new_c] != 'X' and not check[new_r][new_c]:
                    q.append((new_r, new_c))
                    check[new_r][new_c] = True
                    map_distance[new_r][new_c] = map_distance[r][c] + 1
        return -1
    for i in range(len(map_arr)):
        for j in range(len(map_arr[i])):
            if map_arr[i][j] == 'S':
                start_pos = [i, j]
            elif map_arr[i][j] == 'L':
                l_pos = [i, j]
            elif map_arr[i][j] == 'E':
                end_pos = [i, j]
    lever_distance = bfs(start_pos[0], start_pos[1], 'L')
    if lever_distance == -1:
        return -1
    end_distance = bfs(l_pos[0], l_pos[1], 'E')
    if end_distance == -1:
        return -1
    return end_distance