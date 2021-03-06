#try/except

#Determines whether an arbitrary text string can be converted to a number.

def convert_to_num(string):
    try:
        number = int(string)
        print("Converted string %s to number %i." % (string, number))
    except ValueError:
        print("String %s cannot be converted to a number." % (string))

convert_to_num("1234")
convert_to_num("4lex")

def alt_convert(string):
    if string.isdigit():
        number = int(string)
        print("Converted string %s to number %i." % (string, number))
    else:
        print("String %s cannot be converted to a number." % (string))

alt_convert("1234")
alt_convert("4lex")

#Reads several lines of text.

import sys

def read_multi_lines():
    multi_lines = []
    print("Please enter your text. Press Ctrl-C to exit.")
    try:
        while True:
            line = input()
            multi_lines.append(line)
    except KeyboardInterrupt:
        print("\nYour inputs:", multi_lines)
        print("\nThank you. Goodbye\n")
        sys.exit()

read_multi_lines()
