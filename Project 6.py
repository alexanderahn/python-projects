#The os and other Modules

#Prints the filenames of zero length files. And prints the count of zero length files.

import os
files_dir = '/Applications/Python'
count = 0
for files, dirs, root in os.walk(files_dir):
    for f in files:
        files_path = os.path.join(root, f)
        length = os.path.getsize(files_path)
        if length == 0:
            print(f)
            count += 1
print("There are %i files with zero length." % (count))

#Lists and counts all of the images in a given HTML web page/file.

import re
import urllib.request
web_page = urllib.request.urlopen('http://url.com')
html_page = web_page.read()
reimage = re.compile (rb'<img [^>]+')
images = reimage.findall(html_page)
count = len(images)
print(images)
print("The number of images on this page is %i." % (count))
