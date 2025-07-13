#1번부터 각각의 다른 노드까지의 최소 비용을 구해야하는 문제 -> 다익스트라 알고리즘
#이미 방문한 노드의 인접 노드 중 방문하지 않고 가중치가 가장 낮은 노드를 선택해 탐색

from collections import defaultdict
import heapq

def solution(N, road, K):
    edges = defaultdict(list)
    
    for r in road:
        a,b,t = r
        edges[a].append([t,b]) # t값을 기준으로 heapq.pop() 
        edges[b].append([t,a])
    
    heap = [[0,1]]
    heapq.heapify(heap)
    
    answer = [float("inf")] * N
    answer[0] = 0 
    
    while heap:
        current_time , node =  heapq.heappop(heap)
        for time,next_node in edges[node]:
            if answer[next_node-1] > current_time + time:
                answer[next_node-1] = current_time + time
                heapq.heappush(heap,[current_time + time,next_node])        
    
    return len([t for t in answer if t <= K])