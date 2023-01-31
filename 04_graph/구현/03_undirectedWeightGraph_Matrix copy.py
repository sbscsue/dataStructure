N_NODE = int(input())
N_EDGE = int(input())

graph = [[]  for __ in range(N_NODE)]


for i in range(N_EDGE):
    n1,n2,w = list(map(int,input().split(" ")))
    graph[n1].append([n2,w])
    graph[n2].append([n1,w])

print(graph)