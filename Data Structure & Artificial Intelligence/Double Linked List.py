class Node:
    def __init__(self,d):
        self.d=d
        self.next=None
        self.prev=None

class doublelinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.index=0
    def prepend(self,d):
        n=Node(d)
        n.next=self.head
        if self.tail==None:
            self.tail=n
        if self.head!=None:
            self.head.prev=n
        self.head=n
        self.index= self.index+1
    def append(self,d):
        n=Node(d)
        if self.head==None:
            self.head=n
        if self.tail!=None:
            self.tail.next=n
        n.prev=self.tail
        self.tail=n
        self.index= self.index+1
    def insert(self,d,i):
        if i >self.index:
            self.append(d)
        elif i <2:
            self.prepend(d)
        else:
            a=1
            cur=self.head
            while a<i:
                cur=cur.next
                a=a+1
            n=Node(d)
            n.next=cur
            n.prev=cur.prev
            cur.prev.next=n
            cur.prev=n
        self.index= self.index+1
    def traverse1(self):
        c=self.head
        while c!=None:
            print(c.d)
            c=c.next
    def traverse2(self):
        c=self.tail
        while c!=None:
            print(c.d)
            c=c.prev
    def remove(self,d):
        if self.head.d==d:
            self.head=self.head.next
            self.head.prev=None
            return
        elif self.tail.d==d:
            self.tail=self.tail.prev
            self.tail.next=None
        else:
            c=self.head
            while c.next!=None:
                if c.next.d==d:
                    c.next=c.next.next
                    c.next.prev=c
                    return
                c=c.next
l=doublelinkedlist()
for i in range(2,36,8):
    l.append(i)
for i in range(3,36,6):
    l.prepend(i)
