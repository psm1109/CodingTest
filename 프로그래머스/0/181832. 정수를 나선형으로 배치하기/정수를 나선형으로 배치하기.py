def solution(n):
    answer =[[n for n in range(1,n+1)]]+[[0]*n for _ in range(n-1)]
    y,x = 0,n-1 #실제로 저장이 시작되기 전 마지막 저장 지점
    num = n+1 #저장이 시작될 번호
    
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    dn = 1
    for i in range(1,n):
        for _ in range(2):
            dy,dx = direction[dn%4]
            for _ in range(n-i):
                y += dy
                x += dx
                answer[y][x] = num
                num += 1
            dn += 1
            
    return answer