import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = list(int(input()) for _ in range(n))
dp = [0] * (k+1)
dp[0] = 1
for i in coins:
    for j in range(i, k+1):
        # 약간 배낭 풀이랑 비슷하다고 보면 됨
        dp[j] += dp[j-i]
print(dp[k])