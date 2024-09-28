import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0
# 행 축 기준 면들 각 높이차를 구해서 겉넓이 구하기 
for i in range(N):
    prev_height = 0
    for j in range(M):
        if arr[i][j] > prev_height:
            answer += arr[i][j] - prev_height
        prev_height = arr[i][j]
# 열 축도 행 축과 마찬가지로 하기
for i in range(M):
    prev_height = 0
    for j in range(N):
        if arr[j][i] > prev_height:
            answer += arr[j][i] - prev_height
        prev_height = arr[j][i]
# 각각 면이기 때문에 *2해주기
answer *= 2

# 위 아래 면은 N * M *2 이므로 더 해주기
u_square = N * M
answer += (2 * u_square)
print(answer)