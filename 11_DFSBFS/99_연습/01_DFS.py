N_NODE = int(input())
N_EDGE = int(input())

graph = [ [] for __ in range(N_NODE)]
for i in range(N_EDGE):
    e1 , e2 = list(map(int,input().split()))
    graph[e1].append(e2)
    graph[e2].append(e1)

for i in graph:
    i.sort()

print(graph)

stack = []
visited = [False for __ in range(N_NODE)]

def dfs(value):
    visited[value] = True
    print(value,end=" -> ")
    
    for i in graph[value]:
        if not visited[i]:
            dfs(i)


dfs(0)

