from collections import deque
import copy

def solution(maps):
    #start->레버 1번, 레버->exit까지 총 2번의 bfs을 진행하고 return 값을 합산
    #레버까지가 일방통행일 경우 결국 다시 돌아와야하는 경우가 있기 때문에 2번 진행하기로함
    
    def bfs(start,target):  
        queue = deque([[start[0],start[1],0]])
        visited = [[0]*rl for _ in range(cl)]
        visited[start[0]][start[1]] = 1
        
        while queue:
            c,r,t = queue.popleft()
            if (c,r) == target:
                return t
            
            for dy,dx in [(-1,0),(0,1),(1,0),(0,-1)]:
                y,x = c+dy,r+dx
                if 0<= y < cl and  0<= x < rl: 
                    if visited[y][x] == 0 and maps[y][x] != "X":
                        queue.append([y,x,t+1])
                        visited[y][x] = 1
        return -1
    
    answer = 0
    cl,rl = len(maps),len(maps[0])
    for c in range(cl):
        for r in range(rl):
            if maps[c][r] == "S": S = (c,r)
            elif maps[c][r] == "L": L = (c,r)
            elif maps[c][r] == "E": E = (c,r)
    
    t1 = bfs(S,L)
    if t1 == -1:
        return -1
    
    t2 = bfs(L,E)
    if t2 == -1:
        return -1
    
    return t1+t2