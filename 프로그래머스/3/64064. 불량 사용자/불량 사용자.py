def solution(user_id, banned_id):
    answer = 0
    check = [False for _ in range(len(user_id))] 
    ban_check = [False for _ in range(len(banned_id))]
    array = set()
    
    def findUser(user, ban_user):
        same = 0
        for i in range(len(user)):
            if ban_user[i] == "*":
                same += 1
            elif ban_user[i] == user[i]:
                same += 1
        if same == len(user):
            return True
        else:
            return False
    def search(banned_start, ban_array):
        if banned_start == len(banned_id):
            if len(ban_array) == len(banned_id):
                # 이렇게 하면 순서상관없이 넣을 수 있구나!
                # tuple로 넣는 방법
                array.add(tuple(sorted(ban_array)))
            return
        for i in range(len(user_id)):
            if len(user_id[i]) == len(banned_id[banned_start]) and not check[i]:
                if findUser(user_id[i], banned_id[banned_start]):
                    check[i] = True
                    search(banned_start + 1,  ban_array + [user_id[i]])
                    check[i] = False
            else:
                continue
    search(0 ,[])
    return len(array)