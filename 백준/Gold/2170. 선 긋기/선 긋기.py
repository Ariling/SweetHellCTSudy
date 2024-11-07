import sys
input = sys.stdin.readline

T = int(input())
lines = []
for _ in range(T):
    lines.append(list(map(int, input().split())))
lines.sort(key=lambda x:(x[0], x[1]))
answer = 0
start = lines[0][0]
end = lines[0][1]
for i in range(1, T):
    if lines[i][0] > end:
        answer += end - start
        start = lines[i][0]
        end = lines[i][1]
    else:
        end = max(end, lines[i][1])
answer += end - start
print(answer)
