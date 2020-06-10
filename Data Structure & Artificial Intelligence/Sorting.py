def bubble_sort(l):
    for i in range(len(l)):
        for j in range(i,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    print(l)

print("---------------------------------\nName : Nauman\nRoll No. : 648\n---------------------------------")
bubble_sort([9,8,7,4,5,6,1,2])

def insertion_sort(l):
    for i in range(len(l)):
        cor=i
        for j in range(i,len(l)):
            if l[cor]>l[j]:
                cor=j
        l[i],l[cor]=l[cor],l[i]
    print(l)

print("---------------------------------\nName : Nauman\nRoll No. : 648\n---------------------------------")
insertion_sort([9,8,7,4,5,6,1,2])

def merge_sort(l):
    if len(l)>1:
        m=len(l)//2
        left=l[:m]
        right=l[m:]
        merge_sort(left)
        merge_sort(right)
        i,j,k=0,0,0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                l[k]=left[i]
                i=i+1
            else]:
                l[k]=right[j]
                j=j+1
            k=k+1
        while i<len(left):
            l[k]=left[i]
            i=i+1
        while j<len(right):
            l[k]=right[j]
            j=j+1
print("---------------------------------\nName : Nauman\nRoll No. : 648\n---------------------------------")     
alist = [54,26,93,17,77,31,44,55,20]
merge_sort(alist)
print(alist)    

def part(l,s,e):
    p=l[s]
    le=s+1
    r=e
    while le<=r:
        while le<=r and l[le]<=p:
            le=le+1
        while le<=r and l[r]>=p:
            r=r-1
        if le<=r:
            l[r],l[le]=l[le],l[r]
    l[r],l[s]=l[s],l[r]
    return r

def quick_sort(l,s,e):
    if s<e:
        pivot=part(l,s,e)
        quick_sort(l,s,pivot-1)
        quick_sort(l,pivot+1,e)        
    return l
l=[5,4,8,1,31,5,2,3]
print("---------------------------------\nName : Nauman\nRoll No. : 648\n---------------------------------")
print(quick_sort(l,0,len(l)-1))
