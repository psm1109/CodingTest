def solution(triangle):
    l = len(triangle)
    dp = [[0]*l for _ in range(l)]
    dp[0][0] = triangle[0][0]
    
    if l > 1:
        dp[1][0],dp[1][1] = dp[0][0] + triangle[1][0],dp[0][0] + triangle[1][1]
    
    for i in range(2,l):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j] + triangle[i][j], dp[i-1][j-1] + triangle[i][j])
    return max(dp[l-1])