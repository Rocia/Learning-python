'''
The sieve of Eratosthenes is a simple algorithm for finding all prime numbers up to a specified integer. It was created by the ancient Greek mathematician Eratosthenes.
The algorithm to find all the prime numbers less than or equal to a given integer n:

    Create a list of integers from two to n: 2, 3, 4, ..., n
    Start with a counter i set to 2, i.e. the first prime number
    Starting from i+i, count up by i and remove those numbers from the list, i.e. 2*i, 3*i, 4*i, aso..
    Find the first number of the list following i. This is the next prime number.
    Set i to the number found in the previous step
    Repeat steps 3 and 4 until i is greater than n. (As an improvement: It's enough to go to the square root of n)
    All the numbers, which are still in the list, are prime numbers
'''
from math import sqrt

def sieve(n):
	# returns all primes between 2 and n	
	primes = list(range(2,n+1))
	max = sqrt(n)
	num = 2
	while num < max:
		i = num
		while i <= n:
			i += num
			if i in primes:
				primes.remove(i)
		for j in primes:
			if j > num:
				num = j
				break			
	return primes

num = int(input("The below program will display the first N prime numbers\nEnter a number N:"))
print(sieve(num))
