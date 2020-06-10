import random
openList=['S']
nodeList={'S':['A','B'],'A':['S','D'],'B':['S','D'],'D':['A','B']}

def goalTest(some_node):
    return some_node=='D'

def moveGen(some_node):
    return nodeList[some_node]

def SS1():
    while len(openList)>0:
        random.shuffle(openList)
        print("Open list contains",openList)
        N=openList.pop()
        print("Picked Node:", N)
        if goalTest(N):
            print("Goal Found")
            return
        else:
            neighbours=moveGen(N)
            print("Neighbours of ",N," are : " ,neighbours)
            for node in neighbours:
                if node not in openList:
                    openList.append(node)
            
    print("Goal Not Found")

SS1()

