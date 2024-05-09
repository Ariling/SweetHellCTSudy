# 큰 수 만들기
def solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()  # 스택의 마지막 숫자가 현재 숫자보다 작으면 제거한다
            k -= 1
        stack.append(num)
    if k != 0:
        stack = stack[:-k]  # k가 0이 아니면, 남은 k만큼 끝에서 제거하는 방법이래
    return ''.join(stack)