#Final Project

#Takes a directory as an argument, and then finds the extension of each file. Then, for each extension found, it prints the number of files with that extension and the minimum, average, and maximum size for files with that extension in the selected directory.

import os, sys

directory = input("Please enter a directory to learn more about the file types it contains: ")
print("\n")

if not os.path.isdir(directory):
    print("Sorry, I cannot find your directory", directory, ".")
    sys.exit()

files_dict = {}

for root, dirs, files in os.walk(directory):
    for file in files:
        if not files_dict.get(os.path.splitext(file)[1]):
            files_dict[os.path.splitext(file)[1]] = []
        files_dict[(os.path.splitext(file)[1])] += [(file, os.path.getsize(os.path.join(root, file)))]

for type in files_dict.keys():
    count = 0
    average = 0
    for file,size in files_dict[type]:
        count += size
        average = count/len(files_dict[type])
    print("The number of files with {} is {}.".format(type, len(files_dict[type])))
    print("The minimum file size with {} is {}.".format(type, sorted(files_dict[type], key=lambda x: x[1])[0][1]))
    print("The average file size with {} is {}.".format(type, average))
    print("The maximum file size with {} is {}.".format(type, sorted(files_dict[type], key=lambda x: x[1])[-1][1]))
    print("\n")

#Tested with /Users/alex.ahn/Documents
