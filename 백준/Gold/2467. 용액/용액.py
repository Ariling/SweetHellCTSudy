import sys
input = sys.stdin.readline
# 이분 탐색이 꼭 mid만 하는 것이 아니구나..?
N= int(input())
arr = list(map(int, input().split()))
ans_arr = [arr[0], arr[N-1]]
ans_leftIdx = 0
ans_rightIdx = N-1
ans = abs(sum(ans_arr))

while ans_leftIdx < ans_rightIdx:
    tmp = arr[ans_leftIdx]+ arr[ans_rightIdx]
    if abs(tmp) < ans:
        ans_arr = [arr[ans_leftIdx], arr[ans_rightIdx]]
        ans = abs(tmp)
        if ans == 0:
            break
    if tmp < 0:
        ans_leftIdx += 1
    else:
        ans_rightIdx -= 1
print(ans_arr[0], ans_arr[1])
