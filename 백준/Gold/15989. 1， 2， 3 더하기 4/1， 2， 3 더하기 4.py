import sys
input = sys.stdin.readline
T = int(input())
arr = [0] * T
for i in range(len(arr)):
    arr[i] = int(input())
max_num = max(arr)
if max_num <= 3:
    for num in arr:
        print(num)
else:
    dp = [0] * (max_num+1)
    dp[1],dp[2],dp[3] = 1, 2, 3
    for i in range(4, len(dp)):
        # 2의 몫 구하기 그래야 2일 경우의 수를 구할 수 있다.
        case2 = i // 2
        # 1의 경우는 1개만 더하면 되고 3으로 더하는 경우는 3을 뺸 뒤에 그 만큼의 DP값을 구하면 된다.
        dp[i] = case2 + 1 + dp[i-3]
    for num in arr:
        print(dp[num])