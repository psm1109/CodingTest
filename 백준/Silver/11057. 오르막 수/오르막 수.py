N =int(input())
a = [[0]*N for _ in range(10)] #각각 앞자리가 0~9인 경우 N자리수까지 오르막수

for i in range(10):
    a[i][0] = 1

for i in range(1,N):
    a[0][i] = sum([a[j][i-1] for j in range(10)]) 
    for j in range(1,10):
        a[j][i] = a[j-1][i] - a[j-1][i-1]

print(sum([a[i][N-1] for i in range(10)]) % 10007)
