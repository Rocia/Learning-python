def HCF(*n):
    n = n.sort()
    smallest = n[0]
    for i in range (1,smallest+1):
     
n1 = int(input("Enter the first number"))
n2 = int(input("Enter the second number"))
print ("HCF of",n1,"and",n2,"is",HCF(n1,n2))
