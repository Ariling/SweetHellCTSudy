def solution(begin, target, words):
    if target not in words:
        return 0
    visited = [False] * len(words)
    answer = 1e9
    def dfs(begin,target,cnt):
        if begin == target:
            nonlocal answer
            answer = min(answer, cnt)
            return
        for i in range(len(words)):
            differ = sum(begin[j] != words[i][j] for j in range(len(begin))) == 1
            if differ == 1 and visited[i] == False:
                visited[i] = True
                dfs(words[i], target, cnt+1)
                visited[i] = False
    dfs(begin, target, 0)
    return answer