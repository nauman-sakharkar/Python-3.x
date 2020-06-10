text = input("Enter the string : ")

def encrypt(normalText):
    cipherText=""
    for i in range(0,len(normalText),2):
        cipherText=cipherText+(normalText[i])
    for i in range(1,len(normalText),2):
        cipherText=cipherText+(normalText[i])
    return cipherText

def decrypt(cipherText):
    normalText=""
    if(len(cipherText)%2==0):
        cipherText=cipherText[:len(cipherText)//2]+" "+cipherText[len(cipherText)//2:]
    for i in range(0,len(cipherText)//2):
        normalText=normalText+cipherText[i]+cipherText[1+i+len(cipherText)//2]
    return (normalText+cipherText[len(cipherText)//2])
a = encrypt(text)
print("Encrypt : ",a)
print("Decrypt : ",decrypt(a))
