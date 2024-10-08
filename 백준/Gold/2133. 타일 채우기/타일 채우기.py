import sys
input = sys.stdin.readline
N = int(input())
dp = [0 for _ in range(31)]
dp[2] = 3
for i in range(4, N+1):
    if i % 2 == 1:
        dp[i] = 0
    else:
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2
print(dp[N])