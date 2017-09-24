# -*- coding: utf-8 -*-
import re

def sample1():
    return re.sub('^(../)+', '', '../../anyfolder')

def main(args):
    print(sample1())


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='re module sample')
    # option params
    parser.add_argument('-v', action='store_true', help='print detail')

    # function
    main(parser.parse_args())
