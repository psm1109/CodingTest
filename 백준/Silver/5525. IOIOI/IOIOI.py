import sys
from collections import deque   
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

Pn = "IO"*N + "I"
arr = deque(S[:N*2+1])
result = 0

if ''.join(arr) == Pn:
    result += 1

for i in range(N*2+1,M):
    arr.append(S[i])
    arr.popleft()
    if ''.join(arr) == Pn:
        result += 1
print(result)