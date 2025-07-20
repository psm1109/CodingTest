import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    works = [-1*work for work in works]
    heapq.heapify(works)
    for _ in range(n):
        heapq.heappush(works,heapq.heappop(works) + 1)
    return sum([pow(work,2) for work in works])