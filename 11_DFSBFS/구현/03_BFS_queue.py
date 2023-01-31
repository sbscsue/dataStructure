import queue
N_N , N_E = list(map(int,input().split(" ")))

graph = [ [] for _ in range(N_N)]
for i in range(N_E):
    e1,e2 = list(map(int,input().split(" ")))
    graph[e1].append(e2) 
    graph[e2].append(e1)

for i in graph:
    i.sort()

print(graph)


visited = [False for __ in range(N_N)]

start = 0
q = queue.Queue()
q.put(start)
visited[start] = True
print(start,end="-> ")

while(q.empty()!= True):
    value = q.get()
    for n in graph[value]:
        if(visited[n]==False):
            q.put(n)
            visited[n] = True
            print(n,end="-> ")


