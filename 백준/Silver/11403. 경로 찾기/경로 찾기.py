import sys

input = sys.stdin.readline
N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if  graph[i][j]: continue
        else: graph[i][j] = float('inf')

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for r in graph:
    for c in r:
        print(0 if c == float('inf') else 1 , end = " ") 
    print()