from collections import deque
def solution(queue1, queue2):
    # 그니깐 이게 queue1의 길이 4배가 될때까지 같은 두 큐 합이 같게 안 나오면 끝난다는 거지 -1 반환
    # 그리고 이걸 같게 하는 방법은 두 큐를 ㄹㅇ 다 더한 다음에
    # 큰 쪽을 빼서 작은 쪽에 붙이는 방식으로 가면 된다. 
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    if (sum1 + sum2) % 2 == 1:
        return -1
    cnt = 0
    # sum은 무작정 쓰면 안 된다! 이러면 터지네..? 이런걸 무작정 쓰면 안 돼나봐
    median = (sum1 + sum2) / 2
    cnt_length = 3 * len(queue1)
    while cnt < cnt_length:
        if sum1 == sum2:
            return cnt
        elif sum1 > sum2:
            number = q1.popleft()
            q2.append(number)
            sum1 -= number
            sum2 += number
        else:
            number = q2.popleft()
            q1.append(number)
            sum2 -= number
            sum1 += number
        cnt += 1
    return -1