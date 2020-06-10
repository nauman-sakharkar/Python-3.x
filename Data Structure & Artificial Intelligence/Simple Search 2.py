import random
openList=['S']
closedList=[]
nodeList={'S':['A','B'],'A':['S','D'],'B':['S','D'],'D':['A','B']}

def goalTest(some_node):
    return some_node=='D'

def moveGen(some_node):
    return nodeList[some_node]

def SS2():
    while len(openList)>0:
        random.shuffle(openList)
        print("Open list contains",openList)
        N=openList.pop()
        closedList.append(N)
        print("Picked Node:", N)
        if goalTest(N):
            print("Goal Found")
            return
        else:
            neighbours=moveGen(N)
            print("Neighbours of ",N," are : " ,neighbours)
            for node in neighbours:
                if (node not in openList) and (node not in closedList):
                    openList.append(node)
            
    print("Goal Not Found")

SS2()

