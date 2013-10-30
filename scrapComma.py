'''
Created on Oct 28, 2013

@author: dan
'''

import sys

def main():
    myfile = open(sys.argv[1])
    newFile = open('scrapped.csv', 'w')
    for line in myfile:
        line = line.split(",,")[0]
        newFile.write(line+"\n")
    
    newFile.flush()
    newFile.close()
    myfile.close()


if __name__ == '__main__':
    main()