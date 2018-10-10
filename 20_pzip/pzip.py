# -*- coding: utf-8 -*-
import sys
import glob
import os
import zipfile
import re

vervose = 0

def gather(path, targets, base):
    base = os.path.abspath(base)
    for dirpath, dirnames, filenames in os.walk(path):
        if(vervose > 0):
            print('files:')
        for filename in filenames:
            filepath = os.path.abspath(os.path.join(dirpath, filename))
            arc_name = eraseOverPath(os.path.relpath(filepath, base))
            if(vervose > 0):
                print(filepath, arc_name)
            targets.append((filepath, arc_name))

        if(vervose > 0):
            print('dirctories:')
        for dirname in dirnames:
            filepath = os.path.join(dirpath, dirname)
            arc_name = eraseOverPath(os.path.relpath(filepath, base))
            if(vervose > 0):
                print(filepath, arc_name)
            targets.append((filepath, arc_name))

def gatherGlob(path, targets, base):
    files = glob.glob(path)
    for file in files:
        filepath = file
        arc_name = eraseOverPath(os.path.relpath(filepath, base))
        if(vervose > 0):
            print(file, filepath, arc_name)
        targets.append((filepath, arc_name))

def create(zipname, targets):
    zip = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
    for filepath, name in targets:
        zip.write(filepath, name)
    zip.close()

def eraseOverPath(path):
    return re.sub('(\.\.\/)+(\.\.)?', '', path)

def main(args):
    if(args.v):
        global vervose
        vervose = 1

    if(vervose > 0):
        print('execute ' + __file__)
        print('args:' + str(args))

    # gather zip targets
    targets = []
    for path in args.pathes:
        if os.path.isdir(path):
            gather(path, targets, args.base)
        else:
            gatherGlob(path, targets, args.base)

    # create zip
    if(args.n):
        create(args.o, targets)

    if(vervose > 0):
        print('created zip! :: ' + args.o)
        print(targets)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='archive to zip.')
    # args
    parser.add_argument('pathes', metavar='path', type=str, nargs='+', help='zipping path')

    # option params
    parser.add_argument('-o', action='store', default='archive.zip', help='output zip filename')
    parser.add_argument('-v', action='store_true', help='print detail')
    parser.add_argument('-n', action='store_false', help='no archive')
    parser.add_argument('--base', action='store', default='./', help='archive base directory(difault "./" it means execute directory)')

    # function
    main(parser.parse_args())
