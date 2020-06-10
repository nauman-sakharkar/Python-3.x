from tkinter import *
from tkinter import messagebox
gui=Tk()
l=[]
z=17
gui.config(bg='SlateBlue1')
def push(a):
    global z
    global l
    if len(l)==10:
        messagebox.showinfo('Important Message','Stack is Full')
    else:
        l.append(a)
        Label(gui,text=str(a),bg='black',fg='white',highlightcolor='white').grid(sticky='S',row=z)
        z=z-1
def push1():
    global z
    global l
    if len(l)==10:
        messagebox.showinfo('Important Message','Stack is Full')
    else:
        a=e.get()
        l.append(a)
        Label(gui,text=str(a),bg='black',fg='white',highlightcolor='white').grid(sticky='S',row=z)
        z=z-1
def isEmpty():
    if len(l)==0:
        messagebox.showinfo('Stack is Empty','True')
    else:
        messagebox.showinfo('Stack is Empty','False')
def pop():
    global z
    if len(l)==0:
        messagebox.showinfo('Important Message','Stack is Empty')
    else:
        Label(gui,text='                    ',bg='black',fg='white').grid(sticky='S',row=z+1)
        z=z+1
        return(l.pop())
def count():
    if len(l)==0:
        messagebox.showinfo('Important Message','Stack is Empty')
    else:
        messagebox.showinfo('Stack is Empty',len(l))
def multipop():
    a=int(e.get())
    for i in range(a):
        if len(l)==0:
            messagebox.showinfo('Important Message','Stack is Empty')
            return
        else:
            pop()
def peek():
    if len(l)==0:
        messagebox.showinfo('Important Message','Stack is Empty')
    else:
        messagebox.showinfo('Important Message',l[-1])
def check():
    a=e.get()
    for n in a:
        if n=='(':
            push('c')
            messagebox.showinfo('Important Message','"(" detected, Pushed "("')
        elif n==')':
            if len(l)==0:
                messagebox.showinfo('Important Message',''''")"detected, but Stack is Empty,
                Incorrect''')
                return
            else:
                pop()
            messagebox.showinfo('Important Message','")" detected, Poped ")"')
    if len(l)==0:
        messagebox.showinfo('Important Message','Correct')
    else:
        messagebox.showinfo('Important Message','Incorrect')
def check3():
    a=str(e.get())
    z=['1','2','3','4','5','6','7','8','9','0']
    y=['+','-','*','/']
    for n in a:
        if n in z:
            push(int(n))
            messagebox.showinfo('Important Message','%s is Integer ,then pushed'%n)
        elif n in y:
            messagebox.showinfo('Important Message','Operator Detected')
            if len(l)==0:
                messagebox.showinfo('Important Message','Incorrect, Extra Operator or less Operand')
                return
            f=pop()
            messagebox.showinfo('Important Message','%s poped'%f)
            if len(l)==0:
                messagebox.showinfo('Important Message','Incorrect, Extra Operator or less Operand')
                return
            c=pop()
            messagebox.showinfo('Important Message','%s poped'%c)
            if n=='+':
                messagebox.showinfo('Important Message','%s + %s'%(c,f))
                f=int(f)+int(c)
            elif n=='-':
                messagebox.showinfo('Important Message','%s - %s'%(c,f))
                f=int(c)-int(f)
            elif n=='/':
                messagebox.showinfo('Important Message','%s / %s'%(c,f))
                f=int(c)/int(f)
            elif n=='*':
                messagebox.showinfo('Important Message','%s * %s'%(c,f))
                f=int(c)*int(f)
            push(f)
            messagebox.showinfo('Important Message','%s is Result which is pushed'%f)
    if len(l)==1:
        gh=pop()
        messagebox.showinfo('Important Message','Final Answer which is Poped = %s'%gh)
        Label(gui,text='Final Answer : %s'%gh,bg='red',fg='yellow').grid(row=26)
    else:
        messagebox.showinfo('Important Message','Incorrect, Extra Operand Detected or less Operator')
    
def check4():
    a=e.get()
    z=['1','2','3','4','5','6','7','8','9','0']
    y=['+','-','*','/']
    for n in a:
        if n in z:
            push(n)
            messagebox.showinfo('Important Message','%s is Integer ,then pushed'%n)
        elif n in y:
            messagebox.showinfo('Important Message','Operator Detected')
            if len(l)==0:
                messagebox.showinfo('Important Message','Incorrect')
                return
            f=pop()
            messagebox.showinfo('Important Message','%s poped'%f)
            if len(l)==0:
                messagebox.showinfo('Important Message','Incorrect')
                return
            c=pop()
            messagebox.showinfo('Important Message','%s poped'%c)
            if n=='+':
                messagebox.showinfo('Important Message','%s + %s'%(c,f))
                f='('+c+'+'+f+')'
            elif n=='-':
                messagebox.showinfo('Important Message','%s - %s'%(c,f))
                f='('+c+'-'+f+')'
            elif n=='*':
                messagebox.showinfo('Important Message','%s * %s'%(c,f))
                f='('+c+'*'+f+')'
            elif n=='/':
                messagebox.showinfo('Important Message','%s / %s'%(c,f))
                f='('+c+'/'+f+')'
            push(f)
            messagebox.showinfo('Important Message','%s is Result which is pushed'%f)
    gh=pop()
    messagebox.showinfo('Important Message','Final Answer which is Poped = %s'%gh)
    Label(gui,text='Final Answer : %s'%gh,bg='red',fg='yellow').grid(row=26)
def check5():
    a=e.get()
    z=['1','2','3','4','5','6','7','8','9','0']
    y=['+','-','*','/']
    for n in a:
        if n in z and len(l)==0:
            push(n)
            messagebox.showinfo('Important Message','%s is Integer and Stack is Empty, then pushed'%n)
        elif n in y:
            push(n)
            messagebox.showinfo('Important Message','Operator Detected, %s is pushed'%n)
        elif n in z:
            messagebox.showinfo('Important Message','%s is Integer and Stack is not Empty'%n)
            f=pop()
            messagebox.showinfo('Important Message','%s poped'%f)
            c=pop()
            messagebox.showinfo('Important Message','%s poped'%c)
            f=c+n+f
            messagebox.showinfo('Important Message','%s Pushed'%f)
            push(f)
    gh=pop()
    messagebox.showinfo('Important Message','Final Answer which is Poped = %s'%gh)
    Label(gui,text='Final Answer : %s'%gh,bg='red',fg='yellow').grid(row=26)     
e=Entry(gui,bg='sienna1',fg='snow',font='bold',selectbackground='green',justify='center')
e.grid(row=0)
e.focus_set()
Label(gui,text='',bg='SlateBlue1').grid(row=1)
Button(gui,text="Push",command=push1,bg='DarkOrchid4',fg='white',activebackground='SpringGreen3',activeforeground='DarkOrchid4').grid(row=2,sticky="W")
Button(gui,text="Pop",command=pop,bg='DarkOrchid4',fg='white',activebackground='SpringGreen3',activeforeground='DarkOrchid4').grid(row=2,sticky="E")
Button(gui,text="Count",command=count,bg='DarkOrchid4',fg='white',activebackground='SpringGreen3',activeforeground='DarkOrchid4').grid(row=3,sticky="N")
Button(gui,text="isEmpty",command=isEmpty,bg='DarkOrchid4',fg='white',activebackground='SpringGreen3',activeforeground='DarkOrchid4').grid(row=3,sticky="W")
Button(gui,text="Peek",command=peek,bg='DarkOrchid4',fg='white',activebackground='SpringGreen3',activeforeground='DarkOrchid4').grid(row=2,sticky="N")
Button(gui,text="Multipop",command=multipop,bg='DarkOrchid4',fg='white',activebackground='SpringGreen3',activeforeground='DarkOrchid4').grid(row=3,sticky="E")
Label(gui,text='',bg='SlateBlue1').grid(row=4)
Label(gui,text='|       STACK      |',bg='black',fg='white').grid(row=5)
Label(gui,text='|     limit : 10     |',bg='black',fg='white').grid(row=6)

for  i in range(8,19):
    Label(gui,text='|                         |',bg='black',fg='white').grid(row=i)
Label(gui,text='| | | | | | | | | | | | | |',bg='black',fg='white').grid(row=18)
Label(gui,text='   Stack Working   ',bg='red',fg='white').grid(row=19)
Label(gui,text='',bg='SlateBlue1').grid(row=20)
Button(gui,text="Check ( )",command=check,bg='DarkOrchid4',fg='white',activebackground='SpringGreen3',activeforeground='DarkOrchid4').grid(row=21,sticky='W')
Button(gui,text="Cal Postfix",command=check3,bg='DarkOrchid4',fg='white',activebackground='SpringGreen3',activeforeground='DarkOrchid4').grid(row=21,sticky='E')
Button(gui,text="Postfix to Infix",command=check4,bg='DarkOrchid4',fg='white',activebackground='SpringGreen3',activeforeground='DarkOrchid4').grid(row=22,sticky='W')
Button(gui,text="Infix to Postfix",command=check5,bg='DarkOrchid4',fg='white',activebackground='SpringGreen3',activeforeground='DarkOrchid4').grid(row=22,sticky='E')
Label(gui,text='''Common Interface for
Multipop and Push''').grid(row=25)
gui.mainloop()
