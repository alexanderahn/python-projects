#Modules

#A regular expression that matches strings that are either all lower case or all upper case.

regexp = re.findall(r'([A-Z][A-Z]+|[a-z][a-z]+)', st)

#A substitution command that changes names like file1, file2, etc. to file01, file02, etc. but does not add a zero to names like file10 or file20.

txt = 'file1, file2, file10, file20'
re.sub(r'file0\1',txt)

#A regular expression that extracts the names of URLs embedded in a string.

regex = re.findall(r'http\w?://\w+.\w+|www.\w+.\w+')

#A function that takes times of the form 00:00:00 (in other words, hours, minutes, and seconds) and converts them to the corresponding number of seconds.

def convert_to_secs(string):

        all_time = string.split(":")

        tot_secs = (int(all_time[0]) * 60 * 60) + (int(all_time[1]) * 60) + int(all_time[2])

        return tot_secs
