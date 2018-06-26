# Import the os module, for the os.walk function
import os
 
# Set the directory you want to start from
rootDir = 'g:\\Archive'
file = open("c:\\temp\\fileStructure.txt", "w")
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
       file.write('\t%s' % fname  + "\n")
       print('\t%s' % fname)


