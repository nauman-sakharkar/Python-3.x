string = "abcdefghijklmnopqrstuvwxyz"
word = input("Enter word: ")
key = int(input("Enter key: "))
encrypt = ""
decrypt = ""
for i in word:
    if i in string:
        c  = (string.index(i) + key) % 26
        encrypt = encrypt + string[c]
print("Encrypt:",encrypt)
for i in encrypt:
    if i in string:
        c  = (string.index(i) - key) % 26
        decrypt = decrypt + string[c]
print("Decrypt:",decrypt)
