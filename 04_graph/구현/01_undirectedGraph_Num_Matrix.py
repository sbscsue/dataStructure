N_G = int(input())
N_E = int(input())    

#!참고자료 
#python 2차원 배열 초기화 https://leedakyeong.tistory.com/entry/Python-2-dimension-list
graph = [[0] * (N_G) for _ in range(N_G)]   

for i in range(N_E):
    e1,e2 = list(map(int,input().split(" ")))   #0부터 시작

    graph[e1][e2] = 1
    graph[e2][e1] = 1

print(graph)




