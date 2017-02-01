#Pg38
from test.test_threading_local import target
values=[1,2,3]
try:
    for x in values:
        print(x,values[x])
except IndexError as target:
    print("Exception:" )
    print(target)
    
'''
1 2
2 3
Exception:
list index out of range
'''
    
#pg39
def f1():
    print ("f1 in")
    f2()
    print("f2 out")
def f2():
    print ("f2 in")
    f3()
    print("f2 out")
def f3():
    print ("f3 in")
    raise ("Bang!")
    print("f3 out")
try:
    f1()
except Exception as reason:
    print(reason)

'''
f1 in
f2 in
f3 in
exceptions must derive from BaseException
'''
    
#39
values =[1,2,3]
x=2 #part of list'''
try:
    y=values[x]
except:
    print("Exception" )
else:
    print("normal",y)
'''normal 3'''
x=5
try:
        y=values[x]
except:
    print ("Exception")
else:
    print ("Normal",y)
'''normal 3
Exception
'''
    
#40
values =[1,2,3]
x=2 #part of list'''
try:
    y=values[x]
except:
    print("Exception" )
finally:
    print("All Done")
x=5
try:
        y=values[x]
except:
    print ("Exception")
finally:
    print ("All Done")
'''All Done
Exception
All Done
'''

#40(2)
values =[1,-2,3]

try:
    for x  in values:
        if x<0:
            raise(ValueError ('''Negative Array Index!!'''))
        print (x)
except ValueError as value:
    print ("Exception:" +str(value))
'''
1
Exception:Negative Array Index!!
'''