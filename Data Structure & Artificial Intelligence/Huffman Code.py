class node:
    def __init__(self,number,name):
        self.left=None
        self.right=None
        self.name=name
        self.number=number
    def search(self,alph,code=''):
        if(self.left!=None and alph in self.left.name):
            code=code+'0'
            return self.left.search(alph,code)
        elif(self.right!=None and alph in self.right.name):
            code=code+'1'
            return self.right.search(alph,code)
        else:
            return code
word="Your are cool bro thanks"
def get_freq(word):
    unique_alphabets=''.join(set(word))
    d={}
    for alphabets in unique_alphabets:
        d[alphabets]=word.count(alphabets)
    return [(d[k],k) for k in d]
freq=get_freq(word)
nodes=[]
while(len(freq)>1):
    freq.sort()
    if(len(freq[0][1])>1):
        for n1 in nodes:
            if(n1.name==freq[0][1]):
                break
    else:
        n1=node(freq[0][0],freq[0][1])
    if(len(freq[1][1])>1):
        for n2 in nodes:
            if(n2.name==freq[1][1]):
                break
    else:
        n2=node(freq[1][0],freq[1][1])
    n=node(n1.number+n2.number,n1.name+n2.name)
    n.left=n1
    n.right=n2
    freq.pop(0)
    freq.pop(0)
    freq.append((n.number,n.name))
    nodes.append(n)
unique_alphabets=''.join(set(word))
print("Symbol\tWeight\tHuffman Code")
l=[]
for alph in unique_alphabets:
    l.append((n.search(alph),word.count(alph),alph))
print(l)
l=(sorted(l, key=lambda x: len(x[0])))
for i in range(len(l)):
    print(l[i][2],'\t',l[i][1],'\t',l[i][0])
