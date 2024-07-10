def solution(triangle):
    answer = 0
    length = len(triangle)
    print(length)
    if length == 1:
        return triangle[0][0]
    elif length == 2:
        return max(triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1])
    else:
        triangle[1][0] = triangle[0][0] + triangle[1][0]
        triangle[1][1] = triangle[0][0] + triangle[1][1]
        for i in range(2, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] = triangle[i-1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
                else:
                    triangle[i][j] = max(triangle[i-1][j-1] + triangle[i][j], triangle[i-1][j] + triangle[i][j])
    answer = max(triangle[len(triangle) - 1])
    return answer