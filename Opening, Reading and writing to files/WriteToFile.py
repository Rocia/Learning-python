import sys

try:
	#open file stream
	file = open(file_name,"w")
except IOerror:
	print("There was an error writing to", file_name)
	sys.exit()

print("enter' ",file_finish)
print (" ' When finished")
while file_text != file_finish:
	file_text = input("enter text:")
if file_text == file_finish:
	#close the file
	file.close
	break
	file.write(file_text)
	file.write("\n")
file.close()
file_name = input("Enter file name")
if len(file_name) == 0:
	print("Next time please enter something")
	sys.exit()
try:
	file = open(file_name,"r")
except IOerror:
	print("there was an error reading the file.")
	sys.exit()
file_text = file.read()
file.close()
print(file_text)
