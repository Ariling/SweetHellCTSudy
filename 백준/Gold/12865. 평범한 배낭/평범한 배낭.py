import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bags = [[0, 0]] # 이걸 넣는 이유를 물어보자..
for _ in range(N):
    W, V = map(int, input().split())
    bags.append((W, V))
dp = [[0] * (K+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        weight = bags[i][0]
        value = bags[i][1]
        if j >= weight:
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][K])
