def solution(m, n, board):
    answer = 0
    block_arr = [list(board[i]) for i in range(m)]
    
    while True:
        destroy_block = []
        for i in range(m-1):
            for j in range(n - 1):
                if block_arr[i][j] != '0' and block_arr[i][j] == block_arr[i+1][j] == block_arr[i][j+1] == block_arr[i+1][j+1]:
                    destroy_block.append((i, j))
        if not destroy_block:
            break
        else:
            while destroy_block:
                i, j = destroy_block.pop()
                block_arr[i][j] = block_arr[i+1][j] = block_arr[i][j+1] = block_arr[i+1][j+1] = '0'
        # 여기가 그 제대로 맞춰두는 곳
        for j in range(n):
            temp_arr = []
            for i in range(m-1, -1, -1):
                if block_arr[i][j] != '0':
                    temp_arr.append(block_arr[i][j])
                    block_arr[i][j] = '0'
            for i in range(m-1, m-1-len(temp_arr), -1):
                    block_arr[i][j] = temp_arr.pop(0)
        
    for block_r in block_arr:
        for block in block_r:
            if block == '0':
                answer += 1
    return answer