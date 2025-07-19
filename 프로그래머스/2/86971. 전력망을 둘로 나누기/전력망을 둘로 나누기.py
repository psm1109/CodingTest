from collections import defaultdict

def count(a,b,edges,visited):
    cnt = 0
    arr = [a]
    while arr:
        node = arr.pop()
        visited[node] = 1
        cnt += 1
        for next_node in edges[node]:
            if next_node != b and visited[next_node] == 0:
                arr.append(next_node)
    return cnt

def solution(n, wires):
    answer = 100
    
    edges = defaultdict(list)
    
    for wire in wires:
        a,b = wire
        edges[a].append(b)
        edges[b].append(a)
        
    for wire in wires:
        a,b = wire
        visited = [0]*(n+1)
        a_linked = count(a,b,edges,visited)
        b_linked = count(b,a,edges,visited)
        
        answer = min(answer,abs(a_linked-b_linked))
    
    return answer