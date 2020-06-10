class Node:
    def __init__(self,d):
        self.d=d
        self.next=None
class Linkedlist:
    def __init__(self):
        self.root=None
    def prepend(self,d):
        n=Node(d)
        n.next=self.root
        self.root=n
    def append(self,d):
        n=Node(d)
        if self.root==None:
            self.root=n
        else:
            cur=self.root
            while cur.next!=None:
                cur=cur.next
            cur.next=n
    def traverse(self):
        cur=self.root
        while cur!=None:
            print(cur.d)
            cur=cur.next
    def search(self,d):
        cur=self.root
        while cur!=None:
            if cur.d==d:
                return(True)
            cur=cur.next
        return(False)
    def delete(self,d):
        cur=self.root
        if cur!=None:
            if cur.d==d:
                self.root=cur.next
            else:
                while cur.next!=None:
                    if cur.next.d==d:
                        cur.next=cur.next.next
                        return
                    cur=cur.next


