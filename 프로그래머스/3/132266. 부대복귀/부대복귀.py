from collections import defaultdict,deque

def solution(n, roads, sources, destination):
    dist = [-1]*n
    road = defaultdict(list)
    for a,b in roads:
        road[a].append(b)
        road[b].append(a)
    
    q = deque([destination])
    dist[destination-1] = 0 
    while q:
        current= q.popleft()
        for nxt in road[current]:
            if dist[nxt-1] == -1:
                dist[nxt-1] = dist[current-1] +1
                q.append(nxt)
                
               
    return [dist[s-1] for s in sources]