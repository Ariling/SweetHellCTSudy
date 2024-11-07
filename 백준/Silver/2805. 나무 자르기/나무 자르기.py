import sys
input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees = sorted(trees, key=lambda x: x)
left = 0
right = trees[N-1]
def getDistance(mid):
    dis = 0
    for tree in trees:
        tem_dis = tree - mid
        if tem_dis > 0:
            dis += tem_dis
    return dis


while left <= right:
    mid = (left + right) // 2
    distance = getDistance(mid)
    if distance < M:
        right = mid - 1
    else:
        left = mid + 1
print(right)