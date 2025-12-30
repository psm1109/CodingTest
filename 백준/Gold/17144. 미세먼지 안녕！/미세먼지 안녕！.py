import sys
input  = sys.stdin.readline
R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 상단 위치
ac = [A[i][0] for i in range(R)].index(-1)

dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]  # 좌상우하

for _ in range(T):
    #미세먼지 확산
    B = [[0]*C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if A[y][x] > 4:
                D = A[y][x] // 5
                cnt = 0
                for i in range(4):
                    ny, nx = y+dy[i], x+dx[i]
                    if 0 <= ny < R and 0 <= nx < C and A[ny][nx] != -1:
                        B[ny][nx] += D
                        cnt += 1
                B[y][x] += A[y][x] - D*cnt
            else:
                B[y][x]+=A[y][x]
    A = B

    #공기청정기 상단 회전
    for i in range(ac-1,0,-1):
        A[i][0] = A[i-1][0]
    A[0][:-1] = A[0][1:C]
    for i in range(ac):
        A[i][-1] = A[i+1][-1]
    A[ac][2:C] = A[ac][1:-1]
    A[ac][1] = 0
    
    #공기청정기 하단 회전
    for i in range(ac+2,R-1):
        A[i][0] = A[i+1][0]
    A[R-1][:-1] = A[R-1][1:C]
    for i in range(R-1,ac+1,-1):
        A[i][-1] = A[i-1][-1]
    A[ac+1][2:C] = A[ac+1][1:-1]
    A[ac+1][1] = 0
  

print(sum(map(sum, A)) + 2)