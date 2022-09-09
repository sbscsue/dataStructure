N_G = int(input())
N_E = int(input())   


graph = [ [] for _ in range(N_G)]

for i in range(N_E):
    e1,e2 = list(map(int,input().split(" ")))
    graph[e1].append(e2) 
    graph[e2].append(e1)

print(graph)



