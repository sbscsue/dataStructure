N_NODE = int(input())
N_EDGE = int(input())

graph = [[0] * N_NODE for __ in range(N_NODE)]

print(graph)
for i in range(N_EDGE):
    n1,n2,w = list(map(int,input().split(" ")))
    graph[n1][n2] = w
    graph[n2][n1] = w


print(graph)