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

visited = [False for __ in range(N_NODE)]

def dfs(start):
    if(visited[start]==False):
        visited[start] = True
        print(start,end="-> ")
        for n in graph[start]:
            dfs(n)

dfs(0)




