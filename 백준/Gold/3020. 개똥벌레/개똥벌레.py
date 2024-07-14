import sys
input = sys.stdin.readline
N, H = map(int, input().split())
differs = [0] * H
result = [0] * H
result_arr = [0, 0]
for i in range(N):
    diff = int(input())
    if i % 2 == 0:
        differs[0] += 1
        differs[diff] -= 1
    else:
        differs[H - diff] += 1
diff_sum = 0
min_cnt = 1e9
min_section = 0
for i in range(H):
    diff_sum += differs[i]
    result[i] = diff_sum
    if result[i] < min_cnt:
        min_cnt = result[i]
        min_section = 1
    elif result[i] == min_cnt:
        min_section += 1
print(min_cnt, min_section)