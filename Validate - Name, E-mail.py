import re
print("-------------------------------------------\nNauman - 648\n-------------------------------------------")
s="Welcome to Python"
print(re.split(r'\s',s))
print(re.split(r't',s))
print(re.split(r'p-r',s))
print(re.split(r'p-r0-9',s))
print(re.match("python",s,re.I))
print(re.search("prog",s,re.I))
print(re.search("python",s,re.I))
print(re.findall("/d",s))
print(re.sub("/D","",s))

print("-------------------------------------------\nNauman - 648\n-------------------------------------------")
a=input("Enter the E-mail : ")
b=re.search("[A-Za-z]+[A-Za-z._0-9]+@+[a-z]+.+[a-z]",a)
if b :
    print("Valid E-mail")
else:
    print("Inalid E-mail")


a=input("Enter the Contact Number : ")
b=re.search("\d{10}",a)
if b:
    print("Valid Contact Number")
else:
    print("Invalid Contact Number")


a=input("Enter the Name : ")
b=re.search("[^a-zA-z]",a)
if b :
    print("Invalid Name")
else:
    print("Valid Name")
