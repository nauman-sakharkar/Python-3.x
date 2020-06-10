p = int(input("Enter the Publicly Shared Prime : "))
g = int(input("Enter the Publicly Shared Base : "))

a = 6    #aliceSecretKey
b = 15   #bobSecretKey

A = (g**a)%p #Alice sends A
B = (g**b)%p #Alice sends B

ka = (A**b)%p
kb = (B**a)%p


if(ka==kb):
    print("Successful, Secret key :",ka)

else:
    print("Failed")
