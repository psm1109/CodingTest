#크레인의 경우 배열을 돌면서 request 값과 일치하는 항목 출고
#지게차의 경우 배열을 전부 순회하기보다는 배열 외부 빈 문자열 ""를 한 겹 둘러싸고 bfs 또는 dfs로 빈 문자열인 부분만 찾아내고 빈 문자열과 맞닫는 부분 중 request[0] 값과 일치하는 부분이 있다면 출고

def solution(storage, requests):
    n,m = len(storage),len(storage[0])
    answer = n * m 
    storage = [["" for _ in range(m+2)]] + [[""]+list(s)+[""] for s in storage] + [["" for _ in range(m+2)]]
    
    dy,dx = [-1,1,0,0],[0,0,-1,1]
    
    for request in requests:
        if len(request) == 2: #크레인
            for i in range(n+2):
                for j in range(m+2):
                    if storage[i][j] == request[0]:
                        storage[i][j] = ""
                        answer -= 1
        else: #지게차
            stack = [[0,0]]
            visited=[[0]*(m+2) for _ in range(n+2)]
            visited[0][0] = 1
            while stack:
                cy,cx = stack.pop()
                for i in range(4):
                    y,x = cy+dy[i],cx+dx[i]
                    
                    if y < 0 or y >= n+2 or x < 0 or x >= m+2: #범위밖
                        continue
                        
                    if visited[y][x]: #방문
                        continue
                    
                    if storage[y][x] == request:  #출고
                        storage[y][x] = ""
                        answer -= 1
                    elif storage[y][x] == "":
                        stack.append([y,x])
                    visited[y][x] = 1
                    
    return answer