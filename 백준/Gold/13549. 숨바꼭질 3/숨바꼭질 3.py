import sys
from collections import deque
input = sys.stdin.readline
N , K = map(int, input().split())
MAX = 10**5
check = [False] * (MAX+1)
arr = [0] * (MAX+1)
def bfs(n):
    q = deque([])
    q.append(n)
    check[n] = True
    while q:
        s = q.popleft()
        if s == K:
            return arr[s]
        for i in (s*2, s-1, s+1):
            if 0 <= i <= MAX and not check[i]:
                if i == s*2:
                    arr[i] = arr[s]
                else:
                    arr[i] = arr[s] + 1
                check[i] = True
                q.append(i)
print(bfs(N))