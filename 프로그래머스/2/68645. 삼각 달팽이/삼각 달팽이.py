# 삼각 달팽이
def solution(n):
    # 2차원 배열 만드는 방법
    array = [[0] * n for i in range(n)]
    finish_num = int(n * (n+1) / 2)
    num = 1
    i = 0
    j = 0
    array[i][j] = num
    while num < finish_num:
        while i + 1 < n and array[i+1][j] == 0:
            i += 1
            num += 1
            array[i][j] = num
        while j + 1 < n and array[i][j+1] == 0:
            j += 1
            num += 1
            array[i][j] = num
        while (i-1 >= 0 and j-1 >= 0) and array[i-1][j-1] == 0:
            i -= 1
            j -= 1
            num += 1
            array[i][j] = num
    # 이렇게 하면 되는구나?
    answer = [num for row in array for num in row if num != 0]
    return answer