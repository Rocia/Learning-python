'''
Let a and b be two successive Fibonacci numbers with a prior to b. The Fibonacci sequence starting with the number "a" looks like this:

0              a
1              b
2          a + b	
3	        a + 2b
4 	     2a + 3b
5        3a + 5b
6        5a + 8b

We can see that the Fibonacci numbers appear as factors for a and b. The n-th element in this sequence can be calculated with the following formula:

F(n) = Fib(n-1)* a + Fib(n) * b

From this we can conclude that for a natural number n, n>1, the following holds true:

Fib(2*n + 1) = Fib(n)**2 + Fib(n+1)**2
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
print(" index of a |    a |     b | sum of squares | index ")	
print("=====================================================")
for i in range(15):
	square = fib(i)**2 + fib(i+1)**2
	print( " %10d |  %3d |   %3d | %14d | %5d " % (i, fib(i), fib(i+1), square, find_index(square)))



'''
Dummy Output:
 index of a |    a |     b | sum of squares | index 
=====================================================
          0 |    0 |     1 |              1 |     1 
          1 |    1 |     1 |              2 |     3 
          2 |    1 |     2 |              5 |     5 
          3 |    2 |     3 |             13 |     7 
          4 |    3 |     5 |             34 |     9 
          5 |    5 |     8 |             89 |    11 
          6 |    8 |    13 |            233 |    13 
          7 |   13 |    21 |            610 |    15 
          8 |   21 |    34 |           1597 |    17 
          9 |   34 |    55 |           4181 |    19 
         10 |   55 |    89 |          10946 |    21 
         11 |   89 |   144 |          28657 |    23 
         12 |  144 |   233 |          75025 |    25 
         13 |  233 |   377 |         196418 |    27 
         14 |  377 |   610 |         514229 |    29 

'''
