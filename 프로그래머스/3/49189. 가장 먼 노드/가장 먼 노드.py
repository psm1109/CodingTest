from collections import defaultdict,deque
 
def solution(n, vertex):
    # 서로 연결된 노드를 노드별로 정리
    edges = defaultdict(list)
    for n1,n2 in vertex:
        edges[n1].append(n2)
        edges[n2].append(n1)
    
    lengths = [0]*n   #1~n까지
    queue = deque(edges[1])
    #1과 연결된 노드까지의 거리 1로 설정
    for node in queue:
        lengths[node-1] = 1
    
    while queue:
        current = queue.popleft()
        
        for linked_node in edges[current]:
            if linked_node != 1 and not lengths[linked_node-1]:
                lengths[linked_node-1] = lengths[current-1] + 1
                queue.append(linked_node)
    
    answer = lengths.count(max(lengths))
    return answer