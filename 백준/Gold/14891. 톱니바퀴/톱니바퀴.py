import sys
from collections import deque
input = sys.stdin.readline

s1 = deque(list(map(int, input().strip())))
s2 = deque(list(map(int, input().strip())))
s3 = deque(list(map(int, input().strip())))
s4 = deque(list(map(int, input().strip())))
T = int(input())
cnt = 1
def IsRotate(arr1, arr2):
    if arr1[2] == arr2[6]:
        return False
    return True

def rotate(arr, d):
    if d == -1:
        num = arr.popleft()
        arr.append(num)
    else:
        num = arr.pop()
        arr.appendleft(num)
    return arr


while cnt <= T:
    number, dir = map(int, input().split())
    rotations = [0, 0, 0, 0]  # 각 톱니바퀴의 회전 방향 저장
    rotations[number-1] = dir

    # 회전 여부 및 방향 결정
    if number == 1:
        if IsRotate(s1, s2):
            rotations[1] = -dir
            if IsRotate(s2, s3):
                rotations[2] = dir
                if IsRotate(s3, s4):
                    rotations[3] = -dir
    elif number == 2:
        if IsRotate(s1, s2):
            rotations[0] = -dir
        if IsRotate(s2, s3):
            rotations[2] = -dir
            if IsRotate(s3, s4):
                rotations[3] = dir
    elif number == 3:
        if IsRotate(s3, s4):
            rotations[3] = -dir
        if IsRotate(s2, s3):
            rotations[1] = -dir
            if IsRotate(s1, s2):
                rotations[0] = dir
    else:
        if IsRotate(s3, s4):
            rotations[2] = -dir
            if IsRotate(s2, s3):
                rotations[1] = dir
                if IsRotate(s1, s2):
                    rotations[0] = -dir

    # 실제 회전 수행
    if rotations[0] != 0:
        rotate(s1, rotations[0])
    if rotations[1] != 0:
        rotate(s2, rotations[1])
    if rotations[2] != 0:
        rotate(s3, rotations[2])
    if rotations[3] != 0:
        rotate(s4, rotations[3])

    cnt += 1
answer = 0
if s1[0] == 1:
    answer += 1
if s2[0] == 1:
    answer += 2
if s3[0] == 1:
    answer += 4
if s4[0] == 1:
    answer += 8
print(answer)

