plainText = input("Enter the plain text : ")
rows = int(input("Enter the no of rows : "))
columns = int(input("Enter the no of columns : "))
cipherMatrix = []
pos = 0
for i in range(rows):
    l=[]
    for j in range(columns):
        if(pos<len(plainText)):
            l.append(plainText[pos])
        else:
            l.append('')
        pos = pos + 1
    cipherMatrix.append(l)
order = []
print("Enter the order of cols you want to view them in : ")
for i in range(columns):
    s = "Enter choice "+str(i+1)+" : "
    a = int(input(s))
    order.append(a)
cipherText = ""
for i in order:
    for j in range(rows):
        cipherText = cipherText+cipherMatrix[j][i-1]
print("=====================================================")
print("Cipher Text :",cipherText)
