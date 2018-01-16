'''
The Fibonacci numbers are hidden inside of Pascal's triangle. 
If you sum up the coloured numbers of the following triangle, you will get the 7th Fibonacci number:
1
1    1
1    2    1
1    3    3    1
1    4    6    4    1
1    5    10    10    5    1
1    6    15    20    15    6    1
'''
def fib_pascal(n,fib_pos):
    if n == 1:
        line = [1]
        fib_sum = 1 if fib_pos == 0 else 0
    else:
        line = [1]
        (previous_line, fib_sum) = fib_pascal(n-1, fib_pos+1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
        if fib_pos < len(line):
            fib_sum += line[fib_pos]
    return (line, fib_sum)

def fib(n):
    return fib_pascal(n,0)[1]

# and now printing out the first ten Fibonacci numbers:
for i in range(1,10):
    print(fib(i))
