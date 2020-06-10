string = "abcdefghijklmnopqrstuvwxyz"
word = input("Enter word: ")
key = input("Enter key: ")
encrypt = "";
decrypt = "";
for i in range(len(word)):
    value = (string.index(word[i]) + string.index(key[i])) % 26
    encrypt = encrypt + string[value]
print("Encrypt:",encrypt)
for i in range(len(word)):
    value = (string.index(encrypt[i]) - string.index(key[i])) % 26
    decrypt = decrypt + string[value]
print("Decrypt:",decrypt)
