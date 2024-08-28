from collections import deque

def solution(board):
    start_x = 0
    start_y = 0
    board_arr = [list(items) for items in board]
    len_r = len(board_arr)
    len_c = len(board_arr[0])
    for i in range(len_r):
        for j in range(len_c):
            if board_arr[i][j] == 'R':
                start_x = i
                start_y = j
                break
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = set()
    q = deque()
    q.append((start_x, start_y, 0))
    visited.add((start_x, start_y))
    while q:
        r, c, move = q.popleft()
        if board_arr[r][c] == 'G':
            return move
        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]
            while 0 <= new_r < len_r and 0 <= new_c < len_c and board_arr[new_r][new_c] != 'D':
                new_r += dr[i]
                new_c += dc[i]
                # visited.add((new_r, new_c))
            # 조건 이전 위치로 되돌려놓기
            new_r -= dr[i]
            new_c -= dc[i]
            if (new_r, new_c) not in visited:
                visited.add((new_r, new_c))
                q.append((new_r, new_c, move+1))
                
    return -1
    