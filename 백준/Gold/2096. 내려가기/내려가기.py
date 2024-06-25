import sys
input = sys.stdin.readline
T = int(input())
# row가 3인건 고정이니깐
maxdp = [0] * 3
mindp = [0] * 3

for i in range(1, T+1):
    arr = list(map(int, input().split()))

    if i == 1:
        maxdp = arr.copy()
        mindp = arr.copy()
    else:
        max0, max1 = maxdp[0], maxdp[1]
        min0, min1 = mindp[0], mindp[1]

        maxdp[0] = arr[0] + max(maxdp[0], maxdp[1])
        maxdp[1] = arr[1] + max(maxdp[1], max(max0, maxdp[2]))
        maxdp[2] = arr[2] + max(max1, maxdp[2])

        mindp[0] = arr[0] + min(mindp[0], mindp[1])
        mindp[1] = arr[1] + min(mindp[1], min(min0, mindp[2]))
        mindp[2] = arr[2] + min(min1, mindp[2])

max_value = max(maxdp)
min_value = min(mindp)

print(f"{max_value} {min_value}")