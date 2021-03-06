#Assignments and Control Structures

#A for loop that prints the keys and corresponding values of a dictionary in the alphabetical order of the keys.

phonebook = {'John':'615-1356', 'Alex':'881-3921', 'Chad':'999-0889'}
names = phonebook.keys()
for name in sorted(names):
    print(name, phonebook[name])

#Rewrite the following code using a while loop instead of a for loop.

"""a = [7,12,9,14,15,18,12]
b = [9,14,8,3,15,17,15]
big = [ ]
for i in range ( len ( a ) ):
    big.append ( max ( a [ i ],b [ i ] ) )"""

a = [7,12,9,14,15,18,12]
b = [9,14,8,3,15,17,15]
big = [ ]
i = 0
while i < len(a):
    big.append ( max ( a [ i ],b [ i ] ) )
    i = i + 1
print(big)

#A loop that reads each line of a file. It counts the number of characters in each line and keep track of the total number of characters read. Once it has a total of 1,000 or more characters, it breaks from the loop.

filename = 'myfile'
try:
    f = open(filename,'r')
except IOError:
    print("Couldn't open %s" % filename)
count = 0
for line in f:
    count = count + len(line)
    if count >= 1000:
        break
print(count)

#Modify the program written above so that it doesn't count characters on any line that begins with a pound sign (#).

filename = 'myfile'
try:
    f = open(filename,'r')
except IOError:
    print("Couldn't open %s" % filename)
count = 0
for line in f:
    if not line.startswith("#"):
        count = count + len(line)
        if count >= 1000:
            break
print(count)
