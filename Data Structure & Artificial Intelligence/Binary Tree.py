class Node:
    def __init__(self,d):
        self.d=d
        self.l=None
        self.r=None
    def p(self):
        print(self.d)
        if self.l!=None:
            self.l.p()
        if self.r!=None:
            self.r.p()
    def i(self):        
        if self.l!=None:
            self.l.i()
        print(self.d)
        if self.r!=None:
            self.r.i()
    def po(self):        
        if self.l!=None:
            self.l.po()
        if self.r!=None:
            self.r.po()
        print(self.d)
    def s(self,d):
        if self.d>d and self.l!=None:
            self.l.s(d)
        elif self.d<d and self.r!=None:
            self.r.s(d)
        elif self.d==d:
            print("True")
        else:
            print("False")
    def de(self,d):
        if self.d>d and self.l!=None:
            self.l=self.l.de(d)          
        elif self.d<d and self.r!=None:
            self.r=self.r.de(d)
        elif self.d==d:
            if self.l==None:        
                return self.r
            elif self.r==None:
                return self.l
            else:
                m=self.r.findmin()
                self.d=m.d
                return self.r.de(m.d)
        return self
    def findmin(self):
        if self.l==None :
            return (self)
        else:            
            return(self.l .findmin())      
class BinaryTree:
    def __init__(self):
        self.root=None
    
    def insert(self,d):
        n=Node(d)
        if self.root==None:
            self.root=n
        else:
            cur=self.root
            while True:
                if d>cur.d and cur.r==None:
                    cur.r=n
                elif d<cur.d and cur.l==None:
                    cur.l=n
                elif d>cur.d:
                    cur=cur.r
                elif d<cur.d:
                    cur=cur.l
                else:
                    return                
    def preorder(self):
        if self.root!=None:
            cur=self.root
            cur.p()
    def postorder(self):
        if self.root!=None:
            cur=self.root
            cur.po()
    def inorder(self):
        if self.root!=None:
            cur=self.root
            cur.i()
    def search(self,d):
        if self.root!=None:
            cur=self.root
            cur.s(d)
    def delete(self,d):
        if self.root!=None:
            cur=self.root
            cur.de(d)
    
b=BinaryTree()
b.insert(50)
b.insert(10)
b.insert(30)
b.insert(25)
b.insert(52)
b.insert(5)
b.insert(95)
b.insert(85)
b.insert(75)
print(b.search(750))
b.inorder()
b.delete(50)
b.inorder()

