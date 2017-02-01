#start path name with r to indicate this is raw data and not a string, that this data indicates the filepath.
#w=write
def filefunction():
    filename= r"C:\Users\scaela\Desktop\a.txt"
    f=open(filename,"w")
    f.write("hello all\n")
    f.write("Today is a beautiful day")
    f.close()
print(filefunction())
f=open(r"C:\Users\scaela\Desktop\a.txt","r")
line1=f.readline()
line2=f.readline()
print(line1,line2)

'''
None
hello all
 Today is a beautiful day
'''

f=open(r"C:\Users\scaela\Desktop\a.txt","r")
i=1
for line in f:
    print (i,":",line)
i=i+1
f.close()
'''
1 : hello all

1 : Today is a beautiful day
'''

f=open(r"C:\Users\scaela\Desktop\a.txt","r")
i=1
for line in f:
    print (i,":",line.upper())
i=i+1
f.close()
'''
1 : HELLO ALL

1 : TODAY IS A BEAUTIFUL DAY
'''
f=open(r"C:\Users\scaela\Desktop\a.txt","w")
    f.write("abcdefghijklmnopqrstuvwxyz\n")
    f.seek(10,0)
    f.write("Whats Up?")
    f.close()
