import numpy 
key=[["L","G","D","B","A"],
     ["Q","M","H","E","C"],
     ["U","R","N","I","F"],
     ["X","V","S","O","K"],
     ["Z","Y","W","T","P"]]
transposedKey = numpy.transpose(key).tolist()
text = list(input("Enter the plain text : ").upper())
encrypt = ""
for i in range(1, len(text)):
    if(text[i-1] == text[i]):
        text.insert(i, "X")

if(len(text)%2 != 0):
    text.append("X")

def check(a, b, l):
    for i in range(5):
        if(a in l[i] and b in l[i]):
            p1 = (l[i].index(a) + 1) % 5
            p2 = (l[i].index(b) + 1) % 5
            return l[i][p1] + l[i][p2]

for i in range(1, len(text), 2):
    if(check(text[i-1], text[i], key)):
        encrypt = encrypt + check(text[i-1], text[i], key)
    elif(check(text[i-1], text[i], transposedKey)):
        encrypt = encrypt + check(text[i-1], text[i], transposedKey)
    else:
        for j in range(5):
            if(text[i-1] in key[j]):
                p1 = [j, key[j].index(text[i-1])]
            if(text[i] in key[j]):
                p2 = [j, key[j].index(text[i])]
        encrypt = encrypt + key[p1[0]][p2[1]]
        encrypt = encrypt + key[p2[0]][p1[1]]
print("Encrypt:",encrypt)
        
