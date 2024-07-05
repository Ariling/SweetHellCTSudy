def solution(land):
    # 이거 dp를 돌릴수는 없는건가? 
    answer = 0
    n = len(land)
    if n == 1:
        return max(land[0])
    else:
        for i in range(1, len(land)):
            land[i][0] = max(land[i-1][1], land[i-1][2], land[i-1][3]) + land[i][0]
            land[i][1] = max(land[i-1][0], land[i-1][2], land[i-1][3]) + land[i][1]
            land[i][2] = max(land[i-1][0], land[i-1][1], land[i-1][3]) + land[i][2]
            land[i][3] = max(land[i-1][0], land[i-1][1], land[i-1][2]) + land[i][3]
        return max(land[len(land)-1])