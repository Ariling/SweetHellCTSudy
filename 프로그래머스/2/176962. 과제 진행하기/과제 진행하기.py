def solution(plans):
    # 일단 스택을 사용할 것
    answer = []
    # 새로 담을 공간
    arr = []
    for country, start, progress in plans:
        start_arr = start.split(":")
        time = int(start_arr[0]) * 60 + int(start_arr[1])
        arr.append((country, time, int(progress)))
    arr = sorted(arr, key=lambda x: x[1])
    # 아니 배열을 처음부터 돌면서 그 더해보고 아니면 다시 값을 설정해주고
    # 그런 다음에 다음을 가고 시간이 남아 돌면 그때 다시 얘를 꺼내서 실행하고
    # progress가 0이 되면 그냥 냅다 answer에 넣어주고
    # 그렇게 해서 len(arr)과 같을 때까지 시행하라는 거잖아
    current_time = arr[0][1]
    tempor_arr = []
    idx = 0
    while idx < len(arr):
        c, s, p = arr[idx]
        if idx + 1 < len(arr):
            next_start = arr[idx+1][1]
            if current_time + p <= next_start:
                answer.append(c)
                current_time += p
                while tempor_arr and current_time < next_start:
                    prev_c, prev_p = tempor_arr.pop()
                    if current_time + prev_p <= next_start:
                        answer.append(prev_c)
                        current_time += prev_p
                    else:
                        tempor_arr.append((prev_c, prev_p - (next_start - current_time)))
                        break
            else:
                tempor_arr.append((c, p - (next_start - current_time)))
            current_time = next_start
        else:
            answer.append(c)
            current_time += p
            while tempor_arr:
                prev_c, prev_p = tempor_arr.pop()
                answer.append(prev_c)
        idx += 1
    return answer