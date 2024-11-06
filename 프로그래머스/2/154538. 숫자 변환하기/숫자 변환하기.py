from collections import deque
def solution(x, y, n):
    MAX = 10 ** 6
    dp = [0] * (MAX + 1)
    checked = [False] * (MAX + 1)
    q = deque([])
    q.append(x)
    checked[x] = True
    while q:
        s = q.popleft()
        if s == y:
            return dp[s]
        # 이런식으로 할 것! 
        for i in (s+n, s*2, s*3):
            if 0 <= i <= MAX and not checked[i]:
                dp[i] = dp[s] + 1
                checked[i] = True
                q.append(i)
    return -1