#Printing and the Modulus Operator

#Opens a file and prints the length of the longest line in the file.

files = open('testfile', 'r')
length = 0
while 1:
    filename = files.readline()
    if not filename:
        break
    if len(filename) > length
        length = len(filename)
print("The length of the longest line in the file is " + str(length) + ".")
