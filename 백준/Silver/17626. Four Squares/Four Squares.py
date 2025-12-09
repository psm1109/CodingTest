n = int(input())
dp = [0] * (n+1)

i = 1
while i*i <= n:  
    dp[i*i] = 1
    i += 1

for i in range(1, n+1):
    if dp[i] == 0:
        dp[i] = dp[i-1] + 1

        j = 2
        while j*j <= i:
            dp[i] = min(dp[i], dp[i-j*j] + dp[j*j])
            j+=1

print(dp[-1])