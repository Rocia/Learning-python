
def makechecker(s):
    if s=="even":
        return lambda n: n%2
    elif s=="positive":
        return lambda n:n>=0
even= makechecker("even")
print(even(4))
'''0'''

#currying of function
def mult(a,b):
    return a*b
def multby(f,x):
    return lambda y: f(x,y)
double=multby(mult,2)
print(double(4))
'''8'''

#combinator function
nlist= range(1,6)
print(nlist)
def iseven(x):
    return x%2!=0
filter(iseven,nlist)
list(filter(lambda x:x%2 == 0, nlist))
print(list(filter(lambda x:x%2 == 0, nlist)))
'''
range(1, 6)
[2, 4]
'''

nlist= range(1,6)
print(nlist)
def isodd(x):
    return x%2!=0
filter(isodd,nlist)
list(filter(lambda x:x%2 != 0, nlist))
print(list(filter(lambda x:x%2 != 0, nlist)))

'''
range(1, 6)
[1, 3, 5]'''