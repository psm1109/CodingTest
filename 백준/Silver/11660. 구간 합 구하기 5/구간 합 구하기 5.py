import sys
input = sys.stdin.readline

N,M =map(int,input().split())
B = [list(map(int,input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = B[0][0]
for i in range(1,N):
    dp[0][i] = B[0][i] + dp[0][i-1] 
for i in range(1,N):
    dp[i][0] = B[i][0] + dp[i-1][0]
for i in range(1,N):
    for j in range(1,N):
        dp[i][j] = B[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        
for _ in range(M):
    x1,y1,x2,y2 = map(lambda x: int(x)-1, input().split())
    result = dp[x2][y2]
    if y1 and x1:
        result -= (dp[x2][y1-1] + dp[x1-1][y2] - dp[x1-1][y1-1])
    elif x1:
        result -= dp[x1-1][y2]
    elif y1:
        result -= dp[x2][y1-1]
    print(result)