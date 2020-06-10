print("---------------------------------\nName : Nauman\nRoll No. : 648\n---------------------------------")     

class Stack:
    def __init__(self):
        self.l=[]
    def push(self,e):
        self.l.append(e)
    def Pop(self):
        if not(self.isEmpty()):
            return(self.l.pop())
    def isEmpty(self):
        print(self.l==[])
    def peek(self):
        if not(self.isEmpty()):
            print(self.l[-1])

s=Stack()
s.push(5)
s.push(4)
s.push(12)
s.push(54)
s.Pop()
s.Pop()
s.peek()
s.Pop()
s.isEmpty()
s.Pop()
s.isEmpty()
