import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
time = 0
arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])

for [start, end] in arr:
    if start >= time:
        time = end
        result += 1
print(result)
