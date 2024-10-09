from collections import deque
def solution(board):
    # bfs로 하되 dp랑 섞어야 하는 문제였음..
    # 방향성도 그럼 저장을 하면서 돌아야 하나..?
    # 시작점은 치면 안되므로!
    INF = int(1e9)
    N = len(board) - 1
    # 3차원 dp하는 방법.. 이걸 또 초기화 하는 방법은 아래와 같았음
    dp = [[[INF] * 4 for _ in range(len(board))] for _ in range(len(board))]
    def bfs(x, y):
        q = deque([])
        q.append((x,y,0,-1))
        for i in range(4):
            dp[0][0][i] = 0
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        while q:
            r, c, cost, direction = q.popleft()
            if r == len(board)-1 and c == len(board)-1:
                continue
            for i in range(4):
                newX = r + dx[i]
                newY = c + dy[i]
                if 0 <= newX < len(board) and 0 <= newY < len(board) and board[newX][newY] != 1 :
                    new_cost = cost
                    # 이거 잘 알아두기
                    new_cost += 100 if direction == -1 or i == direction else 600
                    if new_cost < dp[newX][newY][i]:
                        dp[newX][newY][i] = new_cost
                        q.append((newX, newY, new_cost, i))
    bfs(0, 0)
    answer = min(dp[N][N])
    return answer