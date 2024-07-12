import math
def solution(numbers):
    answer = 0
    num_list = list(numbers)
    checked = [False] * len(num_list)
    arr = set()
    def dfs(current):
        nonlocal checked
        if current:
            arr.add(int(current))
        for i in range(len(checked)):
            if not checked[i]:
                checked[i] = True
                dfs(current+num_list[i])
                checked[i] = False
    dfs("")
    for num in arr:
        check = True
        if num == 1 or num == 0:
            continue
        else:
            era = int(math.sqrt(num))
            for j in range(2, era + 1):
                if num % j == 0:
                    check = False
                    break
            if check:
                answer += 1
    return answer