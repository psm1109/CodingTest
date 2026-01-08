N,K = map(int,input().split()) 
items = [list(map(int,input().split())) for _ in range(N)] 
dp = [0]*(K+1) 

for W,V in items:
    for i in range(K,W-1,-1):
        dp[i] = max(dp[i],dp[i-W]+V)

print(dp[K])

