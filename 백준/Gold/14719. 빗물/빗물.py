import sys
input = sys.stdin.readline
# 높이, 길이
H , W = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
# s를 0부터 시작을 하고 max를 만나면 그 이후부터 시작을 하는 걸로 잡고 answer를 구하는 방식으로 가야겠다.
# 만약 그 뒤에 max가 없다면 e부터 시작을 해서 하면 될 것 같긴 한데..
for i in range(1, W-1):
    left_max = max(arr[:i])
    right_max = max(arr[i+1:])

    compare = min(left_max, right_max)
    if arr[i] < compare:
        ans += compare - arr[i]
print(ans)