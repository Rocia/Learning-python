''' iterative fibonacci '''
def fibi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
num = int(input("Enter Number"))
print(fibi(num))
