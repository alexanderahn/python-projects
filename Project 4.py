#Functions

#A function that accepts the name of a file and returns a tuple containing the number of lines, words, and characters that are in the file.

def filecount(filename):
    '''filecount(filename) returns a tuple
    containing the number of lines, words,
    and characters that are in the file.'''

    try:
        f = open(filename, 'r')
    except IOError:
        print("Couldn't open %s" % filename)

    text = f.readlines()
    f.close()

    linecount = wordcount = charcount = 0
    for i in text:
        linecount = linecount + 1
        wordcount = wordcount + len(i.split())
        charcount = charcount + len(list(i))

    return tuple(linecount, wordcount, charcount)

#A function that accepts an arbitrary number of lists and returns a single list with exactly one occurrence of each element that appears in any of the input lists.

def merge(*args):
    '''merge(*args) returns a merged list
    with exactly one occurence of each
    element that appears in any of the
    input lists.'''

    mergedlist = []
    for i in args:
        for l in i:
            if l not in mergedlist:
                mergedlist.append(l)

    return list(mergedlist)

print(merge([1,2,3,4], [1,2,8,9]))

#Using the map function to add a constant to each element of a list. Perform the same operation using a list comprehension.

addwithmap = list(map(lambda x:x + 1,numlist))

'''addwithcom'''
[x + 1 for x in numlist]

#A function that takes a variable number of lists. Each list can contain any number of words. Returns a dictionary where the words are the keys and the values are the total count of each word in all of the lists

def total_dict(*args):
    '''totdic(*args) returns a dictionary
    where the words of the input lists
    are the keys, and the values are
    they total count of each word in
    all lists.'''
    out = {}
    for list in args:
        for item in list:
            if item in out.keys():
                out[item] = out[item] + 1
            else:
                out[item] = 1
    return out

wl1 = ["double", "triple", "int", "quadruple"]
wl2 = ["double", "home run"]
wl3 = ["int", "double", "float"]

print(total_dict(wl1, wl2, wl3))

#A function that combines several dictionaries by creating a new dictionary with all the keys of the original ones. If a key appears in more than one input dictionary, the value corresponding to that key in the new dictionary should be a list containing all the values encountered in the input dictionaries that correspond to that key.

def mergedict(*args):
    '''mergedict returns a new dictionary
    with all the keys of the original
    input dictionaries. The duplicate keys
    list all values that correspond to it.'''

    argslists = list(args)
    alldicts = []
    allkeys = []
    returndict = {}

    for i in argslists:
        allkeys += i.keys()
        alldicts.append(i)

    for i in allkeys:
        if not returndict.get(i):
            returndict[i] = []

    for emdict in alldicts:
        for key, value in emdict.items():
            returndict[key] = returndict[key] + [value]
    return returndict
