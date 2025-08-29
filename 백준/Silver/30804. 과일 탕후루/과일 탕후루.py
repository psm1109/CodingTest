import sys
input = sys.stdin.readline

N = int(input())
t = list(map(int, input().split()))

l = 0 #왼쪽 포인터
fruits = [0]*10 #과일 개수를 저장할 배열
k = 0 #과일 종류 
result = 0 #최대 길이

for r in range(N):
    if fruits[t[r]] == 0:
        k += 1
    fruits[t[r]] += 1

    while k > 2:
        fruits[t[l]] -= 1
        if fruits[t[l]] == 0:
            k -= 1
        l += 1
    
    result = max(result,r-l+1)

print(result)
