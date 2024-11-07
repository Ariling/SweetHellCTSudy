import sys
input = sys.stdin.readline

N = int(input())
students = list(map(int, input().split()))
dp = [0] * (N+1)
for i in range(1, N+1):
    for j in range(i):
        # j+1부터 i까지가 하나의 조가 된다는 것..
        max_val = max(students[j:i])
        min_val = min(students[j:i])
        dp[i] = max(dp[i], dp[j] + max_val - min_val)
print(dp[N])