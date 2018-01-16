'''
recursive factorial program taking user inputs
'''
def factorial(n):
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        return res	
num = int(input("Enter a number:"))
print(factorial(num))
