def solution(maps):
    def search(x,y):
        days = 0
        arr = [[y,x]]
        visited[y][x] = 1
        while arr:
            cy, cx = arr.pop()
            days += int(maps[cy][cx])
            for i in range(4):
                ny,nx = cy+dy[i],cx+dx[i]
                if ny < 0 or nx < 0 or ny >= len_y or nx >= len_x:
                    continue
                if maps[ny][nx] == "X" or visited[ny][nx]:
                    continue
                arr.append([ny,nx])
                visited[ny][nx] = 1
                
        return days
    
    answer = []
    len_y,len_x = len(maps),len(maps[0])
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    visited = [[0]*len_x for _ in range(len_y)]
    for i in range(len(maps)):
        for j in range(len(maps[0])):  
            if maps[i][j] != "X" and visited[i][j] == 0:
                answer.append(search(j,i))
                
                
    return sorted(answer) if answer else [-1]