'''
Write Python program for finding the second largest element in an array A of size n using Tournament Method. Discuss Time complexity.
'''
groups=[]
def tournament(l):
    global groups
    ll=[]
    if(len(l)==1):
        return l[0]
    if(len(l)%2==0):
        for i in range(0,len(l)-1,2):
            if(l[i]>l[i+1]):
                ll.append(l[i])
            else:
                ll.append(l[i+1])
            groups.append((l[i],l[i+1]))
    else:
        for i in range(0,len(l)-2,2):
            if(l[i]>l[i+1]):
                ll.append(l[i])
            else:
                ll.append(l[i+1])
            groups.append((l[i],l[i+1]))
        ll.append(l[-1])
    return(tournament(ll))

def main_tournament(l,n):
    for i in range(n):
        global groups
        winner = tournament(l)
        l=[min(item) for item in groups if(winner in item)]
        groups=[]
    return(winner)

