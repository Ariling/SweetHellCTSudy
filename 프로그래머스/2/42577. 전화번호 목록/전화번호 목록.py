def solution(phone_book):
    answer = True
    dict = {}
    # 이거는 자릿수로 판결을 내면 될 듯! 
    # 그리고 이거 정렬 해야 해 , len을 기준으로 정렬하자 -> 이렇게 하면 되는구나! 
    phone_book = sorted(phone_book, key=lambda x: (len(x), x))
    for phone in phone_book:
        for i in range(1, len(phone)):
            prefix = phone[:i]
            if prefix in dict:
                return False
        dict[phone] = 1
    
    return answer