import math
def solution(k, d):
    answer = 0
    x = 0
    while x <= d:
        y = math.ceil(math.sqrt((d**2) - (x**2)) // k) + 1
        answer += y
        x += k
    return answer