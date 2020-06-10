print("---------------------------------\nName : Nauman\nRoll No. : 648\n---------------------------------")

class Queue:
    def __init__(self):
        self.l=[]
    def enqueue(self,e):
        self.l.insert(0,e)
    def dequeue(self):
        if not(self.isEmpty()):
            self.l.pop(0)
    def isEmpty(self):
         return(self.l==[])
    def peek(self):
       if not (self.isEmpty()):
           return(self.l[0])
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.peek())
q.dequeue()
print(q.isEmpty())
q.dequeue()
q.dequeue()
q.dequeue()
print(q.isEmpty())
