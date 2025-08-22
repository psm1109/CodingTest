def solution(n, k, cmds):
    answer = ["O"]*n
    prev = [i-1 for i in range(n)]
    nxt = [i+1 for i in range(n)]
    nxt[-1] = -1
    
    current = k
    deleted = [] #삭제된 행을 저장할 스택
    for cmd in cmds:
        c = cmd.split(" ")
        if c[0] == 'U':
            for _ in range(int(c[1])):
                current = prev[current]
                
        elif c[0] == 'D':
            for _ in range(int(c[1])):
                current = nxt[current]
                
        elif c[0] == "C":
            answer[current] = "X"
            deleted.append((current,prev[current],nxt[current]))
            
            if prev[current] != -1:
                nxt[prev[current]] = nxt[current]
            if nxt[current] != -1:
                prev[nxt[current]] = prev[current]
                
            
            #단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
            if nxt[current] != -1:
                current = nxt[current]
            else:
                current = prev[current]
        
        else: #Z
            #원래대로 복구할 행이 없을 때(즉, 삭제된 행이 없을 때) "Z"가 명령어로 주어지는 경우는 없습니다.
            col,pv,nt = deleted.pop()
            answer[col] = "O"
            if pv != -1:
                nxt[pv] = col
            if nt != -1:
                prev[nt] = col
            
    return ''.join(answer)