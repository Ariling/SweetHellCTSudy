answer = 0
def solution(numbers, target):
    n = len(numbers)
    def dfs(idx, result):
        global answer
        if idx == n:
            if result == target:
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0, 0)
    return answer