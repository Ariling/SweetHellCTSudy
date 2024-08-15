def solution(dirs):
    position = set()
    r, c = 0, 0
    for dir in dirs:
        startR, startC = r, c
        if dir == "U" and r < 5:
            r += 1
        elif dir == "D" and r > -5:
            r -= 1
        elif dir == "L" and c > -5:
            c -= 1
        elif dir == "R" and c < 5:
            c += 1
        if startR == r and startC == c:
            continue
        else:
            position.add((min(startR,r), min(startC, c), max(startR,r), max(startC, c)))
    return len(position)