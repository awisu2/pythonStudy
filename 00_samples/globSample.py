# -*- coding: utf-8 -*-
import sys
import glob
import os

def searchFiles(path):
    files = glob.glob('/Users/ohtaniyuichi/Dropbox/develop/')
    for file in files:
        if os.path.isdir(file):
            print('D:' + file)
        else:
            print('F:' + file)

def main():
    if(len(sys.argv) < 2):
        print('please set any arg for path')
        return
    searchFiles(sys.argv[1])

if __name__ == '__main__':
    main()
