def linear_search(l,e):
    for i in l:
        if i==e:
            print("Yes")
            break
    else:
        print("No")

def binary_search(l,el):
    s=0
    e=len(l)-1
    while s<=e:
        m=(s+e)//2
        if l[m]==el:
            print("Yes")
            return
        elif l[m]>el:
            e=m-1
        else:
            s=m+1
    print("No")
