print("---------------------------------\nName : Nauman\nRoll No. : 648\n---------------------------------")     

class Linear_Sets:
    def __init__(self):
        self.l=[]
    def insert(self,e):
        if e not in self.l:
            self.l.append(e)
    def union(self,b):
        u=self.l[:]
        for i in b.l:
            if i not in u:
                u.append(i)
        print(u)
    def intersection(self,b):
        i=[]
        for j in self.l:
            if j in b.l:
                i.append(j)
        print(i)
    def difference(self,b):
        d=self.l[:]
        for i in b.l:
            if i in d:
                d.remove(i)
        print(d)
    def issubset(self,b):
        for i in self.l:
            if i not in b.l:
                print(False)
                return
        print(True)
    
s=Linear_Sets()
s.insert(1)
s.insert(151)
s.insert(11)
s.insert(1)
t=Linear_Sets()
t.insert(1)
s.difference(t)
s.issubset(t)
