'''
Write Python program for checking whether a given graph G has simple path from source s to
destination d. Assume the graph G is represented using adjacent matrix.

To get to the shortest from all the paths, we use a little different approach as shown below.
In this, as we get the path from the start node to the end node, we compare the length of the path with a
variable named as shortest which is initialized with the None value. If the length of generated path is less than
the length of shortest, if shortest is not None, the newly generated path is set as the value of shortest. Again, if there is no path, it returns None
'''
graph={'A' : ['B','C'],
           'B':['C','D'],
           'C':['D'],
           'D':['E'],
           'E':['F'],
           'F':['C']}
def find_all_path(graph,start,end,path=[]):
    path = path + [start]
    if start==end:
        return [path]
    if start not in graph:
        print("No path")
        return None
    paths=[]
    for node in graph[start]:
        if node not in path:
            newpaths=find_all_path(graph,node,end,path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
    
print(find_all_path(graph,'A','F'))
