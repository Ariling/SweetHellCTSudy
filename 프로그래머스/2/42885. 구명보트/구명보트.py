def solution(people, limit):
    people.sort(key=lambda x: x)
    start , end = 0, len(people)-1
    answer = 0
    while start <= end:
        if start == end:
            answer += 1
            break
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        answer += 1
    return answer