def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2])
    parent = [i for i in range(n)]
    
    #사이클 탐색
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    for s,e,g in costs:
        fs,fe = find(s),find(e)
        if fs == fe:
            continue
        else:
            parent[fe] = fs
            answer += g
        
    return answer