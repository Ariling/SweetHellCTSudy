import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
diff = [0] * (N+1)
for _ in range(M):
    first, end, amount = map(int, input().split())
    diff[first-1] += amount
    diff[end] -= amount
result = [0] * N
curr_sum = 0
for i in range(N):
    curr_sum += diff[i]
    result[i] = arr[i] + curr_sum
# 이런 방법도 있네..?
print(*result)