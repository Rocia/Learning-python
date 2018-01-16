'''
recursive function find_index(), should return the index of a number in the Fibonacci sequence, 
if the number is an element of this sequence and returns -1 if the number is not contained in it, 

i.e.
fib(find_index(n)) == n
'''

memo = {0:0, 1:1}
def fib(n):
    if not n in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

def find_index(*x):
	""" finds the natural number i with fib(i) = n """
	if len(x) == 1:
		# started by user
		# find index starting from 0
		return find_index(x[0],0)
	else:
		n = fib(x[1])
		m = x[0]
		if  n > m:
			return -1
		elif n == m:
			return x[1]
		else:
			return find_index(m,x[1]+1)
num = int(input("Enter N:"))
print(fib(find_index(num)))
