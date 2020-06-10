# dijkstra's algorithm
graph = [ 
          [0,8,0,0,5],
          [0,0,1,0,2],
          [0,0,0,4,0],
          [7,0,6,0,0],
          [0,3,9,2,0]
        ]

graph_edges = list()
for i in range(len(graph)):
    for j in range(len(graph)):
        graph_edges.append((i+1,j+1,graph[i][j]))
        graph_edges.append((j+1,i+1,graph[i][j]))
graph_edges = list(set(graph_edges))

source = 1
possible = []
already_visited = []
for edge in graph_edges:
    if source == edge[0] and edge[2]!=0:
        possible.append(edge)

path = {}
for i in range(len(graph)):
    path[i+1] = float("inf")

for p in possible:
    edges = [p]
    path[p[1]] = p[2]
    already_visited = []
    cost = 0
    while edges:
        edge = edges.pop(0)
        cost = cost + edge[2]
        already_visited.append(edge)
        next_stop = edge[1]
        if path[edge[1]]>cost:
            path[edge[1]] = cost
        edges.extend([edge for edge in graph_edges if next_stop == edge[0] and edge[2]!=0 and not (edge in already_visited and path[edge[1]]<cost)])

path[source] = 0
print("Shortest path")
for i,v in path.items():
    print("From",source," to ",i," : ",0 if v==float("inf") else v)

