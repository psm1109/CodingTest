import sys
import heapq

input = sys.stdin.readline
N = int(input())
heap = []
for _  in range(N):
    x = int(input())
    if x:
        heapq.heappush(heap,-x)
    else:
        print(heapq.heappop(heap)*-1 if heap else 0)