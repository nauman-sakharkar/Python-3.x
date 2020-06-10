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
        return(self.l==[])
    def peek(self):
        if not(self.isEmpty()):
            return(self.l[-1])

s=Stack()
a=input("Enter the Postfix for Evaluation : ")
l=a.split(' ')
for i in l:
    if i in '+-*/':
        b=s.Pop()
        a=s.Pop()
        c=eval(a+i+b)
        s.push(str(c))
    else:
        s.push(i)
print(s.Pop())

a=input("Enter the Infix Expression : ")
l=a.split(' ')
p=''
b={'+':1,'-':1,'*':3,'/':4,'(':0}
for i in l:
    if i in '+-*/':
        while (not s.isEmpty()) and b[i]<=b[s.peek()]:
            p=p+s.Pop()
        s.push(i)
    elif i=='(':
        s.push(i)
    elif i==')':
        while s.peek()!='(':
            p=p+s.Pop()
        s.Pop()
    else:
        p=p+i
while not s.isEmpty():
    p=p+s.Pop()
print(p)
