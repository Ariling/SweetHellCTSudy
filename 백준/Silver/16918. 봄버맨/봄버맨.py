import sys
input = sys.stdin.readline
R, C, N = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(R)]
# 2초, 4초마다 다음과 같음(짝수)
bomb_arr = [['O']*C for _ in range(R)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def change_arr():
    destroy_arr = [['O'] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O':
                destroy_arr[i][j] = '.'
                for dir in range(4):
                    r = i + dr[dir]
                    c = j + dc[dir]
                    if 0 <= r < R and 0 <= c < C:
                        destroy_arr[r][c] = '.'
    return destroy_arr
for i in range(1,N+1):
    if i == 1:
        continue
    elif i % 4 == 2 or i % 4 == 0:
        continue
    else:
        arr = change_arr()

if N % 4 == 2 or N % 4 == 0:
    for row in bomb_arr:
        print(''.join(row))
else:
    for row in arr:
        print(''.join(row))