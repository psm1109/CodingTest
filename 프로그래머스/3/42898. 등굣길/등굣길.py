def solution(m, n, puddles):
    answer = 0
    road = [[0]*m for _ in range(n)]
    road[0][0] = 1
    
    for puddle in puddles:
        x,y = puddle
        road[y-1][x-1] = -1
        
    for i in range(n):
        for j in range(m):
            if road[i][j] == -1:
                road[i][j] = 0
            else:
                if i>0:
                    road[i][j] += road[i-1][j]
                if j>0:
                    road[i][j] += road[i][j-1]
       
    return road[n-1][m-1] % 1000000007