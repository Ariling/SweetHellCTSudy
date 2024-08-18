import math
def solution(numbers):
    answer = 0
    check = [False] * len(numbers)
    number_set = set()
    def dfs(idx, number):
        if number:
            number_set.add(int(number))
        
        if idx == len(numbers):
            return
        
        for i in range(len(numbers)):
            if not check[i]:
                check[i] = True
                dfs(idx + 1, number + numbers[i])
                check[i] = False
        
    dfs(0, "")
    while number_set:
        number = number_set.pop()
        if number == 0 or number == 1:
            continue
        era = int(math.sqrt(number))
        check = True
        for j in range(2, era + 1):
            if number % j == 0:
                check = False
                break
        if check:
            answer += 1
        
    return answer