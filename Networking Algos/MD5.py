import hashlib  
text = input("Enter word: ")
result = hashlib.md5(text.encode())  
print(result.hexdigest()) 
