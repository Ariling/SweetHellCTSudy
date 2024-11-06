import sys
input = sys.stdin.readline
N = int(input())
dp = 0
while N >= 0:
    if N % 5 == 0:
        dp += (N // 5)
        print(dp)
        break
    N -= 3
    dp += 1
else:
    print(-1)