def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
    
    def check(y,x):
        s = set()
        s.add((y,x))
        while s:
            Y,X = s.pop()
            if Y >= m-1 or X >= n-1:
                continue
                
            if board[y][x] == board[Y+1][X] == board[Y][X+1] == board[Y+1][X+1]:
                s.add((Y+1,X))
                s.add((Y,X+1))
                s.add((Y+1,X+1))
                remove_block.add((Y,X)) 
                remove_block.add((Y+1,X)) 
                remove_block.add((Y,X+1)) 
                remove_block.add((Y+1,X+1)) 
    
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
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == "" : 
                    continue
                remove_block = set()
                check(i,j) #제거할 블럭 확인
                for y,x in remove_block: #블럭 제거
                    board[y][x] = ""
                    cnt += 1
        if cnt == 0:
            break
        answer += cnt
        board = gravity(board) #블럭 떨어트리기
        
    return answer