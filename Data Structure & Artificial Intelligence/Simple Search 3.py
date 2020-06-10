import random
openList=[['S',None]]
closedList=[]
#nodeList={'S':['A','B','C'],'A':['S','B','E'],'B':['S','D'],'C':['S','D','G'],'D':['B','C','G'],'E':['A','G'],'G':['D','C','E']}

nodeList={'S':['A','B'],'A':['S','D'],'B':['S','D'],'D':['A','B']}

def goalTest(some_node):
    return some_node=='D'

def moveGen(some_node):
    return nodeList[some_node]

def SS3():
    while len(openList)>0:
        random.shuffle(openList)
        print("Open list contains",openList)
        seen=openList.pop()
        N=seen[0]
        closedList.append(N)
        print("Picked Node:", N)
        if goalTest(N):
            print("Goal Found")
            print(seen)
            return
        else:
            neighbours=moveGen(N)
            print("Neighbours of ",N," are : " ,neighbours)
            for node in neighbours:
                if (node not in openList) and (node not in closedList):
                    l=[node,seen]
                    openList.append(l)
            
    print("Goal Not Found")

SS3()

