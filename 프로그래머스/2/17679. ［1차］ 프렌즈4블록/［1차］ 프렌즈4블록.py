def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
    
    def gravity(board):
        for x in range(n):
            stack = []
            for y in range(m):
                if board[y][x] != "":
                    stack.append(board[y][x])
        
            for y in range(m-1, -1, -1):
                if stack:
                    board[y][x] = stack.pop()
                else:
                    board[y][x] = ""
        return board
        
    while 1:
        cnt = 0
        remove_block = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == "" : 
                    continue
                
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    remove_block.update({(i,j),(i+1,j),(i,j+1),(i+1,j+1)})
            
        for y,x in remove_block: #블럭 제거
            board[y][x] = ""
            cnt += 1
            
        if cnt == 0:
            break
        answer += cnt
        board = gravity(board) #블럭 떨어트리기
        
    return answer