def solution(numbers):
    answer = ''
    arr = list(map(str, numbers))
    arr.sort(key=lambda number: number*3, reverse=True)
    return str(int(''.join(arr)))