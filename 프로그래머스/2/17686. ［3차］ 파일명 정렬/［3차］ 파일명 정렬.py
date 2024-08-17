def solution(files):
    # HEAD는 숫자 이전까지면 되.. 이거는 알겠어
    # 숫자도 숫자까지만 아는 그걸 찾으면 되 (최대 5숫자니깐 그것만 알면 될테고.. 아니 근데 제대로 한 건데 그러면?)
    # TAIL은 그냥 아무 상관이 없는거고? 그냥 순서대로만 들어오면 된다. 얘를 순서에 맞게 하면 된다는 거지?
    # 그러면 정렬을 lambda x : x[1] 
    compare_list = []
    for file in files:
        number_put = False
        number_start = 0
        number_end = 0
        for i in range(len(file)):
            if number_put == False and file[i].isdigit():
                if not file[i-1].isdigit():
                    number_start = i
                if i == len(file) - 1 or not file[i+1].isdigit() or (i - number_start) == 4 :
                    number_end = i + 1
                if number_start != 0 and number_end != 0:
                    number_put = True
        compare_list.append((file, file[:number_start].lower(), file[number_start : number_end]))
    compare_list = sorted(compare_list, key=lambda x : (x[1], int(x[2])))
    answer = []
    for compare in compare_list:
        answer.append(compare[0])
    return answer