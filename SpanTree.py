graph = [(13,1,3),(2,1,5),(11,1,2),(15,2,3),(8,2,4),(12,2,5),(14,4,5)]
graph.sort()

for edge in graph:
    print("From Edge ",edge[1]," To Edge",edge[2]," : ",edge[0])
print("=================")

def notCyclic(tree,start,dest):
    edges = []
    tree = tree[:]
    while tree:
        a,b = tree[0][0],tree[0][1]
        for i in range(1,len(tree)):
            if a in tree[i] or b in tree[i]:
                tree[i] = tree[i] + (a,b,)
        else:
            edges.append(tree.pop(0))
    for e in edges:
        if str(start) in e and str(dest) in e:
            return False
    return True

spantree = []
cost = 0
for edge in graph:
    if notCyclic(spantree,edge[1],edge[2]):
        print("Edge (",edge[1],",",edge[2],") with cost:",edge[0])
        cost = cost + edge[0]
        spantree.append((str(edge[1]),str(edge[2])))
print("Total cost:",cost)
