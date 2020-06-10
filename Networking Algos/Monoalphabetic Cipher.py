string = "abcdefghijklmnopqrstuvwxyz"
random = "okmutigeyfbaqhncjdplwxsvzr"
word = input("Enter word: ")
encrypt = ""
decrypt = ""
for i in word:
    if i in string:
        encrypt = encrypt + random[string.index(i)]
print("Encrypt:",encrypt)
for i in encrypt:
    if i in random:
        decrypt = decrypt + string[random.index(i)]
print("Decrypt:",decrypt)
