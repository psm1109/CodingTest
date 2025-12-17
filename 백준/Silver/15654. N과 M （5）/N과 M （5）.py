N,M = map(int,input().split())
arr = sorted(map(int,input().split()))

visited = [False]*N

def dfs(stack):
    if len(stack) == M:
        print(*stack)
        return 
    
    for i in range(N):
        if visited[i] == True:
            continue
        stack.append(arr[i])
        visited[i] = True
        dfs(stack)
        stack.pop()
        visited[i] = False

dfs([])
