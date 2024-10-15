import sys
input = sys.stdin.readline

N, dis = map(int, input().split())
dis_arr = []
for _ in range(N):
    st, ed, cost = map(int, input().split())
    dis_arr.append((st, ed, cost))
dis_arr = sorted(dis_arr, key=lambda x: (x[0], -x[1], x[2]))
result = int(1e9)
def find_road(cur_dis, current_cost, idx):
    global result
    # 끝내는 조건들
    if current_cost > result:
        return
    if cur_dis > dis:
        return
    if cur_dis == dis and current_cost < result:
        result = current_cost
        return
    # 현재 위치에서 목표 지점까지 직접 가는 경우를 항상 고려
    if current_cost + (dis - cur_dis) < result:
        result = current_cost + (dis - cur_dis)

    if idx == len(dis_arr):
        return
    # 돌면서 재귀돌리기
    for i in range(idx, len(dis_arr)):
        st, ed, cost = dis_arr[i]
        if cur_dis > st:
            continue
        if cur_dis <= st:
            find_road(ed, (st-cur_dis)+cost+current_cost, i+1)
            find_road(cur_dis, current_cost, i+1)
find_road(0, 0, 0)
print(result)