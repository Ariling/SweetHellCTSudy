def solution(distance, rocks, n):
    # 누가 봐도 너무 커서 이분탐색인지는 알겠어...
    rocks = sorted(rocks)
    rocks.append(distance)
    # 왜냐면 그 만큼 없앤다음에 저 거리를 구하고... 그 다음에 비교해서 하는 방식인거잖아..
    # 그리고 알아낸 점 ! 이분탐색은 굳이 거리를 진짜 구할 필요가 없다.
    # 그냥 누적을 시키고 mid에 충족을 하냐 안하냐가 중요한 것!
    left, right = 0, distance
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        # 거리를 나타내기
        dis = 0
        # 중간 거리까지의 거리
        break_pnt = 0
        # 거리의 최솟값
        result = 1e9
        remove_cnt = 0
        for rock in rocks:
            dis = rock - break_pnt
            if dis < mid:
                remove_cnt += 1
            else:
                if result > dis:
                    result = dis
                break_pnt = rock
                dis = 0
        result = min(result, dis)
        # 이건 불가능하다는 것이니 업데이트를 여기다 하면 안 된다.
        if remove_cnt > n:
            right = mid - 1
        else:
            # answer은 항상 mid로 업데이트하기 ^^;;
            answer = mid
            left = mid + 1
    return answer