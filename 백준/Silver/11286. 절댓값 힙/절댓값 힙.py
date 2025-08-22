import sys
import heapq

input = sys.stdin.readline
N = int(input())

heap = []
for _ in range(N):
    x = int(input())
    if x: #1
        heapq.heappush(heap,(abs(x),1 if x>0 else -1)) #부호를 같이 넣음
    else: #2
        if heap:
            num = heapq.heappop(heap)
            print(num[0]*num[1])
        else:
            print(0)