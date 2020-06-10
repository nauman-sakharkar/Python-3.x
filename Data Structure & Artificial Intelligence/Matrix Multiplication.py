'''
Write Python program to perform matrix multiplication. Discuss the complexity of algorithm used.
The definition of matrix multiplication is that if C = AB for an n × m matrix A and an m × p matrix B, then C is an n × p matrix with entries.
A simple algorithm can be constructed which loops over the indices i from 1 through n and j from 1 through p, computing the
above using a nested loops.
This algorithm takes time for the inputs of all square matrices of size n × n is Θ(n3), i.e., cubic in Big O notation.
'''
def matmult(m1,m2):
    m3=[]
    for i in range(len(m1)):
        l=[]
        for j in range(len(m2[0])):
            result=0
            for k in range(len(m2)):
                result += m1[i][k] * m2[k][j]
            l.append(result)
        m3.append(l)
    return m3
r1=int(input("Enter the row of Matrix 1 : "))
c1=int(input("Enter the column of Matrix 1 : "))
r2=int(input("Enter the row of Matrix 2 : "))
c2=int(input("Enter the column of Matrix 2 : "))
m1=[]
for i in range(r1):
    l=[]
    for j in range(c1):
        l.append(int(input("Enter the number : ")))
    m1.append(l)
m2=[]
for i in range(r2):
    l=[]
    for j in range(c2):
        l.append(int(input("Enter the number : ")))
    m2.append(l)
result=matmult(m1,m2)
print("Result of a Matrix multiplication")
for i in range(len(result)):
    print(result[i])
