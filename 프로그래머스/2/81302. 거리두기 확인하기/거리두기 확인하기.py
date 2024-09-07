def solution(places):
    answer = []
    def isPossible(place):
        arr = [list(item) for item in place]
        student_position = []
        for x in range(len(arr)):
            for y in range(len(arr[x])):
                if arr[x][y] == 'P':
                    student_position.append((x, y))
        if len(student_position) == 0:
            return 1
        else:
            for x in range(len(student_position)):
                for y in range(x+1, len(student_position)):
                    rx, cx = student_position[x]
                    ry, cy = student_position[y]
                    x_diff = abs(rx - ry)
                    y_diff = abs(cx - cy)
                    if x_diff + y_diff == 1:
                        return 0
                    elif x_diff + y_diff == 2:
                        if rx != ry and cx != cy:
                            if arr[rx][cy] != 'X' or arr[ry][cx] != 'X':
                                return 0
                        elif rx == ry:
                            if arr[rx][(cx + cy) // 2] != 'X':
                                return 0
                        elif cx == cy:
                            if arr[(rx + ry) // 2][cx] != 'X':
                                return 0
                    else:
                        continue
        return 1
    for place in places:
        answer.append(isPossible(place))
    return answer