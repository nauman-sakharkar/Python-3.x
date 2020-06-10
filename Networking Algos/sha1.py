import hashlib  
text = input("Enter word: ")
result = hashlib.sha1(text.encode())  
print(result.hexdigest()) 
