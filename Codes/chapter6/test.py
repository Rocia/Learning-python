import re
drink=r"Pepsi|Limca|Sprite"
request="get me some Pepsi"
if re.search(drink, request):
    print("You must be over 21")
else:
    print ("ok")
'''You must be over 21'''
#pg54 execute ta home


import re
name="Suven Consultants"
nameRe=r"Suven"
if re.search(nameRe, name, re.IGNORECASE):
    print ("match")
'''match'''
    
import re
imp="888-888-8888"
if re.search(r"\d{3}-\d{2,4}\s\d{4,8}",imp):
    print("match")
else:
    print("no match")
'''no match'''
    
'''Control structures
data structures-nume: int, long complex, float
functions-def, calling,returns, named parameters, (**params), argumers  (*args)
exceptions: try-except try-except-else, try-finally
handling files :creating, closing, writing, seeking
RegEx: define pattern, compile, search
'''

#Capture groups
'''
[\d] ---- 0 or 1
[\d+] ---- 0 or 1 or more
[\D+] ----- 1 or more non digits
'''
import re
getComponents=r"(\D+)(\d+)(\D+)(\d+)"
#here capturing groups whereas in previous work searching for a String
inputText="abcd123defg 456"
matchResults= re.search(getComponents, inputText)
captureGroups= matchResults.groups()
for group in captureGroups:
    print(group)
'''
abcd
123
defg 
456
'''   

#splitting STrings
'''
\w --- WORD
\W --- Nonword
'''

import re
p= re.compile(r"\W+")
s= "200 Main Street"
p.split(s)
print(p.split(s))
'''['200', 'Main', 'Street']
'''

import re
p= re.compile(r"\w+")
s= "200 Main Street"
p.split(s)
print(p.split(s))
'''['', ' ', ' ', '']
'''

import  re
pathSeparator= re.compile(r"/")
pathName="/usr/bin/python"
pathSeparator.split(pathName)
print(pathSeparator.split(pathName))
'''['', 'usr', 'bin', 'python']
'''
import  re
pathSeparator= re.compile(r"/")
pathName="/usr/bin/python"
pathSeparator.split(pathName)[1:]
print(pathSeparator.split(pathName)[1:])
'''['usr', 'bin', 'python']
'''

#search and replace
'''
sub-substitue-gv string that needs to replace gvn string
subn-gv string that needs to replace gvn string + gives count of replacements made
'''
#sub
import  re
pattern=re.compile("(red|green|blue)")
input=" red shirt, yellow shorts, green socks"
pattern.sub("White", input)
print(pattern.sub("White", input))
''' White shirt, yellow shorts, White socks
'''

#subn
import  re
pattern=re.compile("(red|green|blue)")
input=" red shirt, blue shorts, green socks"
pattern.subn("White", input)
print(pattern.subn("White", input))
'''(' White shirt, White shorts, White socks', 3)
'''
