#Date : 23/8/18

graph={"S":["A","B"],"A":["S","D"],"B":["S","D"],"D":["A","B"]}
openList = [["S",None]]
visitedNodes = []

def moveGen(N):
    return graph[N]

def goalTest(N):
    return N=="D"

def SS3():
      while(openList):
            print("Open List : ",openList)
            seen = openList.pop(0)
            N = seen[0]
            visitedNodes.append(N)
            print("Picked Node : ",N)
            if(goalTest(N)):
              print("Goal Found")
              s = ""
              while seen:
                    s += seen.pop(0)+" >-"
                    seen=seen[0]
              s = s[::-1]
              print("Path is : ",s)
              return
            else:
              n = moveGen(N)
              print("Neighbours of ",N,": ",n,"\n===========================================")
              for i in n:
                  if i not in openList and i not in visitedNodes:
                      openList.append([i,seen])
              print(openList)
      print("Goal not Found")
SS3()
