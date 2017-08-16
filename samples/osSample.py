# -*- coding: utf-8 -*-
import os

def sample1():
    #ex:python_study/samples
    return os.path.relpath('./', '../../')

def sample2():
    #ex:../../foo.txt
    return os.path.join('../..', 'foo.txt')

def sample3():
    #ex:../../foo.txt
    return os.path.abspath('./')

def sample4():
    #ex:/Users/ohtaniyuichi/Dropbox/develop/python_study/samples
    abspath = os.path.abspath('./')
    #ex:/Users/ohtaniyuichi/Dropbox/develop/python_study
    path = os.path.abspath(os.path.join(abspath, '../'))
    #ex:python_study
    return os.path.relpath(path, '../../')

def sample5():
    for d, ds, fs in os.walk('.'):
        print('DIRNAME:' + d)
        for d in ds:
            print('DIR:' + d)
        for f in fs:
            print('FILE:' + f)

def sample6():
    d = './'
    f = './' + __file__
    a = './*.py'

    if os.path.isdir(d):
        print(d + ' is directory')
    else:
        print(d + ' is not directory')

    if os.path.isdir(f):
        print(f + ' is directory')
    else:
        print(f + ' is not directory')

    if os.path.isdir(a):
        print(a + ' is directory')
    else:
        print(a + ' is not directory')

    if os.path.isfile(d):
        print(d + ' is file')
    else:
        print(d + ' is not file')

    if os.path.isfile(f):
        print(f + ' is file')
    else:
        print(f + ' is not file')

    if os.path.isfile(a):
        print(a + ' is file')
    else:
        print(a + ' is not file')

def sample7():
    #ex: ../../anyfolder
    return os.path.relpath('../../anyfolder', './')

def main(args):
    print('sample1::')
    print(sample1())
    print('sample2::')
    print(sample2())
    print('sample3::')
    print(sample3())
    print('sample4::')
    print(sample4())
    print('sample5::')
    sample5()
    print('sample6::')
    sample6()
    print('sample7::')
    print(sample7())

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='os module sample')
    # option params
    parser.add_argument('-v', action='store_true', help='print detail')

    # function
    main(parser.parse_args())
