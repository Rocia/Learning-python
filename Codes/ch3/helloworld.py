def myfunc():
    print("HelloWorld")
myfunc()
'''HelloWorld'''

def myf(n):
    return(n*n)
print(myf(5))
'''
HelloWorld
25
'''

def makealist(start,end):
    newlist=list(range(start,end))
    newlist.insert(0,"[")
    return newlist

makealist(5,10)
print(makealist(5,10))

'''['[', 5, 6, 7, 8, 9]
'''


def swap(a,b):
    return b,a 

x,y=swap(10,20)
print(x)
print(y)

'''20
10
'''

def fibb(n):
    a,b=0,1
    while b<n:
        print(b)
        a,b=b,a+b 
    return a
    print(a)
        
fibb(12)
'''1
1
2
3
5
8
'''
print(type(fibb))
'''<class 'function'>
'''

def makeRange(fromVal, toVal=20,step=1):
    return range (fromVal,toVal,step)
print(makeRange(15))
'''range(15, 20)
'''
print(makeRange(15,18))
'''range(15, 18)
'''
print(makeRange(1,5,18))
'''range(1, 5, 18)
'''
#if a function call doesnt hve the parameters then default call takes the parameters
#while calling the function if we give the parameter values then it will take the  precedence over default parameters
def makeRange1(fromVal, toVal=20,step=1):
    return list(range (fromVal,toVal,step))
print(makeRange1(15))

print(makeRange1(15,18))

print(makeRange1(1,5,18))
'''
[15, 16, 17, 18, 19]
[15, 16, 17]
[1]
'''


#named params
'''
named parameters- para value assigned at RuntimeError
used when the no. of parameters to be passed to function isnt known in advance
'''
def named(**params):
    for p in params.keys():
        
        print("param",p,"ha value",params[p])
named(a=1,b=2,c=3)
'''
param c ha value 3
param a ha value 1
param b ha value 2
'''
'''return on the basis of keyvalue pair'''

#pg34
def named2(first,last,**namedParams):
    print("Positional:",first,last)
    print(namedParams)
named2("one","two",thirdArg=3, fourthArg="Four")

'''Positional: one two
{'thirdArg': 3, 'fourthArg': 'Four'}
'''

#pg35
#list and Tuples
def f(*args):
    print("args:",args)
    
a=(1,2,3,4)
b=[1,2,3,4]
f(0,1,2,3,4,5)
f(0,a,5)
f(0,b,5)    
f(0,*a)    
f(0,*b)   
'''
args: (0, 1, 2, 3, 4, 5)
args: (0, (1, 2, 3, 4), 5)
args: (0, [1, 2, 3, 4], 5)
args: (0, 1, 2, 3, 4)
args: (0, 1, 2, 3, 4)
'''
    
    