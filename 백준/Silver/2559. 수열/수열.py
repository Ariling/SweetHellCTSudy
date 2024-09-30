import sys
input = sys.stdin.readline
N, K = map(int,input().split())
arr = list(map(int, input().split()))
# 투 포인터로 가자..
start, end = 0, K-1
if K == 1:
    print(max(arr))
else:
    sum_num = sum(arr[0:K])
    result = sum_num
    start, end = 0, K
    while end < len(arr):
        sum_num -= arr[start]
        sum_num += arr[end]
        end += 1
        start += 1
        if sum_num > result:
            result = sum_num
    print(result)