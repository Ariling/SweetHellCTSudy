import sys
from collections import deque
input = sys.stdin.readline
N ,M = map(int, input().split())
util_arr = []
# 사다리랑 뱀을 차례대로 담음
for _ in range(N+M):
    s, e = map(int, input().split())
    util_arr.append((s, e))
arr = [0] * 101
check = [False] * 101
# check처리 까먹지 말기
def bfs(i):
    q = deque([])
    q.append(i)
    check[i] = True
    while q:
        idx = q.popleft()
        if idx == 100:
            return arr[idx]
        for i in range(1,7):
            pos = idx + i
            if pos > 100 or check[pos]:
                continue
            for s, e in util_arr:
                if s == pos:
                    pos = e
                    break
            if not check[pos]:
                arr[pos] = arr[idx] + 1
                check[pos] = True
                q.append(pos)
print(bfs(1))