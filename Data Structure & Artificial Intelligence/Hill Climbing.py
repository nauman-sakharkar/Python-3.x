openList=[('MUMBAI',790)]
closedList=[]
nodeList={'MUMBAI':[('DELHI',1200),('NASIK',350),('GOA',800),('PUNE',130)],
          'DELHI':[('NASIK',375),('MUMBAI',1200)],
          'NASIK':[('INDORE',400),('DELHI',375),('MUMBAI',350),('NAGPUR',600)],
          'INDORE':[('NASIK',400)],
          'NAGPUR':[('NASIK',600),('PUNE',450)],
          'PUNE':[('MUMBAI',130),('NAGPUR',450),('BANGALORE',550)],
          'BANGALORE':[('PUNE',550),('GOA',750),('HYDERABAD',110)],
          'HYDERABAD':[('GOA',850),('BANGALORE',110)],
          'GOA':[('BANGALORE',750),('HYDERABAD',850),('MUMBAI',800)]
          }
hValue={"HYDERABAD":0,"BANGALORE":110,"GOA":850,"PUNE":660,"NAGPUR":1110,"MUMBAI":790,"DELHI":1515,"NASIK":780,"INDORE":1540}
pickedNode = []

def sort(l):
    for i in range(len(l)-1,-1,-1):
        for j in range(0,i):
            if(l[i][1]<l[j][1]):
                l[i],l[j]=l[j],l[i]
    return l

def goalTest(some_node):
    return some_node=='HYDERABAD'

def moveGen(some_node):
    return nodeList[some_node[0]]

def hill_climbing():
    global openList
    while len(openList)>0:
        N=openList.pop(0)
        closedList.append(N[0])
        #print("Picked Node:", N)
        pickedNode.append(N)
        if goalTest(N[0]):
            print("Goal Found\n=======================================")
            total = 0
            for i in range(1,len(pickedNode)-1):
                print(pickedNode[i-1][0],"->",pickedNode[i][0]," : ",pickedNode[i-1][1]-pickedNode[i][1])
                total+=pickedNode[i-1][1]-pickedNode[i][1]
            print(pickedNode[-2][0],"->",pickedNode[-1][0]," : ",pickedNode[-2][1])
            total += pickedNode[-2][1]
            print("---------------------------------------")
            print("Total distance from Mumbai to Hyderabad: ",total)
            return
        else:
            neighbours=moveGen(N)
            
            for node in neighbours:
                if (node not in openList) and (node[0] not in closedList):
                    t=(node[0],hValue[node[0]])
                    if hValue[N[0]]>hValue[node[0]]:
                        openList.append(t)
            openList = sort(openList)
            openList = openList[0:1]
            #print(openList)
    print("Goal Not Found")

hill_climbing()
#sort([('DELHI',1200),('NASIK',350),('GOA',800),('PUNE',130)])
