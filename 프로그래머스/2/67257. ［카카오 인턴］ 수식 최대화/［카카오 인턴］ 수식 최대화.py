import math
from itertools import permutations
def solution(expression):
    # 이거 경우의 수를 다 따져야 하는 문제인 것 같은데..
    # * - + 이거 왔다갔다하는 문제잖아.. 
    # 6가지해서 할 수 있겠지..
    exp = ["*", "+", "-"]
    exp_list = list(permutations(exp, 3))
    exp_arr = []
    # 숫자를 담기 위한 것
    index = ""
    for i in range(len(expression)):
        # 한 문자 구별자
        char = expression[i]
        if char != "-" and char != "*" and char != "+":
            index = index+char
        else:
            exp_arr.append(int(index))
            index = ""
            exp_arr.append(char)
    exp_arr.append(int(index))
    index = ""
    max_num = -math.inf
    answer = 0
    for i in exp_list:
        stack = exp_arr.copy()
        result = 0
        # 우선 순위가 0 , 1 ,2이렇게 높은 것
        # 그니깐 0이 나올때까지 다 하고
        # 또 그 중에서 2순위 나올때까지 하고 그러라고? 미치겠네...
        # 이건 첫번째 순위 처리
        idx = 1
        while idx < len(stack):
            if stack[idx] == i[0]:
                exp_result = 0
                b = stack.pop(idx+1)
                exp_a = stack.pop(idx)
                a = stack.pop(idx-1)
                if exp_a == '*':
                    exp_result += a * b
                elif exp_a == '+':
                    exp_result += a + b
                else:
                    exp_result += a - b
                stack.insert(idx-1,exp_result)
            else:
                idx += 1
        # 중간 순위 처리
        idx = 1
        while idx < len(stack) - 1:
            if stack[idx] == i[1]:
                exp_result = 0
                b = stack.pop(idx+1)
                exp_a = stack.pop(idx)
                a = stack.pop(idx-1)
                if exp_a == '*':
                    exp_result += a * b
                elif exp_a == '+':
                    exp_result += a + b
                else:
                    exp_result += a - b
                stack.insert(idx-1,exp_result)
            else:
                idx += 1
        # 이건 끝 순위 처리
        while len(stack) > 1:
            exp_result = 0
            a = stack.pop(0)
            exp_a = stack.pop(0)
            b = stack.pop(0)
            if exp_a == '*':
                exp_result += a * b
            elif exp_a == '+':
                exp_result += a + b
            else:
                exp_result += a - b
            stack.insert(0, exp_result)
        result = abs(stack[0])
        if result > max_num:
            max_num = result
    return max_num